from ast import Break
import random
from collections import defaultdict
from collections import Counter
import copy

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k, t, N = [int(_) for _ in dataset.readline().strip().split()]
        Dna = dataset.read().strip().split()
    return Dna, k, t, N 

def RandomSelectKMersMotifs(Dna, k):
    Motifs = []
    for seq in Dna:
        if len(seq) >= k:
            start = random.randint(0, len(seq) - k)
            Motifs.append(seq[start:start + k])
        else:
            Motifs.append(None)  # or handle short strings differently
    return Motifs

def Score(Motifs):
    k = len(Motifs[0])
    total_score = 0
    for i in range(k):
        # Count nucleotides at position i across all kmers
        column = [kmer[i] for kmer in Motifs]
        counts = Counter(column)
        max_count = max(counts.values())  # Most frequent nucleotide
        total_score += max_count  # Number of mismatches

    return total_score

def CreateProfile(kmers):
    if not kmers:
        return {}

    k = len(kmers[0])
    profile = {'A': [1]*k, 'C': [1]*k, 'G': [1]*k, 'T': [1]*k}  # Pseudocount = 1

    for kmer in kmers:
        for i, nucleotide in enumerate(kmer):
            profile[nucleotide][i] += 1

    # Convert counts to probabilities
    total_kmers = len(kmers) + 4  # +4 because we added 1 to each of 4 nucleotides
    for nucleotide in profile:
        profile[nucleotide] = [count / total_kmers for count in profile[nucleotide]]

    return profile

def Pr(text, Profile):
    p = 1
    k = len(text)
    for i in range(k):
        p *= Profile[text[i]][i]
    return p

def Random_Biased(probabilities):
    total = sum(probabilities)
    r = random.uniform(0, total)  # random số thực trong [0, total)
    cumulative = 0
    for i, p in enumerate(probabilities):
        cumulative += p
        if r < cumulative:
            return i

def ProfileMostProbableKMer(Dna, k, Profile):
    maxP = 0
    kmer = ""
    for i in range(len(Dna) - k + 1):
        text = Dna[i:i+k]
        if Pr(text, Profile) >= maxP:
            maxP = Pr(text, Profile)
            #print(text, maxP)
            kmer = text
    return kmer

def GibbsSampler(Dna_list, k, t, N):
    Motifs = RandomSelectKMersMotifs(Dna_list, k)
    BestMotifs = copy.deepcopy(Motifs)
    CurrentProfile = CreateProfile(BestMotifs)
    for i in range(N):
        idx = random.randint(0, t - 1)
        CurrentProfile = CreateProfile([BestMotifs[j] for j in range(t) if j != i])
        p = []
        for j in range(len(Dna_list[0]) - k + 1):
            p.append(Pr(Dna_list[idx][j:j+k], CurrentProfile))
        ChosenIdx = Random_Biased(p)
        Motifs[idx] = Dna_list[idx][ChosenIdx:ChosenIdx + k]
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs           
        #else:
    return BestMotifs

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30309_11.txt"
    Dna, k, t, N = ReadInput(path)
    #print(*RandomizedMotifSearch(Dna, k, t))
    all_best_motifs = []
    for _ in range(20):
        best_motifs = GibbsSampler(Dna, k, t, N)
        all_best_motifs.append(best_motifs)
    best_motifs_overall = max(all_best_motifs, key=Score)
    print(*best_motifs_overall)

if __name__ == main():
    main()
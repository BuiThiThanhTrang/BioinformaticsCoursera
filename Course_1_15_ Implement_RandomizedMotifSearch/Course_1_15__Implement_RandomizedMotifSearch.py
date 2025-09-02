from ast import Break
import random
from collections import defaultdict
from collections import Counter

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k, t = [int(_) for _ in dataset.readline().strip().split()]
        Dna = dataset.read().strip().split()
    return Dna, k, t

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

def RandomizedMotifSearch(Dna_list, k, t):
    BestMotifs = RandomSelectKMersMotifs(Dna_list, k)
    CurrentProfile = CreateProfile(BestMotifs)
    while True:
        CurrentProfile = CreateProfile(BestMotifs)
        Motifs = []
        for Dna in Dna_list:
            Motifs.append(ProfileMostProbableKMer(Dna, k, CurrentProfile))
        if Score(Motifs) > Score(BestMotifs):
            BestMotifs = Motifs           
        else:
            return BestMotifs

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30307_5.txt"
    Dna, k, t = ReadInput(path)
    #print(*RandomizedMotifSearch(Dna, k, t))
    all_best_motifs = []
    for _ in range(1000): 
        best_motifs = RandomizedMotifSearch(Dna, k, t)
        all_best_motifs.append(best_motifs)
    best_motifs_overall = max(all_best_motifs, key=Score)
    print(*best_motifs_overall)

if __name__ == main():
    main()
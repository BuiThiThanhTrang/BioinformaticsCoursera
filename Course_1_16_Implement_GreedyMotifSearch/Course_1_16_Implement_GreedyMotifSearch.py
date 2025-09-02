from ast import Break
import random
from collections import defaultdict
from collections import Counter

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k, t = [int(_) for _ in dataset.readline().strip().split()]
        Dna = dataset.read().strip().split()
    return Dna, k, t

def FirstSelectKMersMotifs(Dna, k):
    Motifs = []
    for seq in Dna:
        Motifs.append(seq[0:k])
  # or handle short strings differently
    return Motifs

def Score(Motifs):
    k = len(Motifs[0])
    total_score = 0
    for i in range(k):
        # Count nucleotides at position i across all kmers
        column = [kmer[i] for kmer in Motifs]
        counts = Counter(column)
        max_count = max(counts.values())  # Most frequent nucleotide
        total_score += len(Motifs) - max_count  # Number of mismatches

    return total_score

def CreateProfile(kmers):
    if not kmers:
        return {}

    k = len(kmers[0])
    profile = {'A': [0]*k, 'C': [0]*k, 'G': [0]*k, 'T': [0]*k} 

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
    kmer = Dna[0:k]
    for i in range(len(Dna) - k + 1):
        text = Dna[i:i+k]
        if Pr(text, Profile) > maxP:
            maxP = Pr(text, Profile)
            #print(text, maxP)
            kmer = text
    return kmer

def GreedyMotifSearch(Dna_list, k, t):
    BestMotifs = FirstSelectKMersMotifs(Dna_list, k)
    Motifs = []
    for i in range(len(Dna_list[0]) - k + 1):
        Motifs.append(Dna_list[0][i:i+k])
        for Dna in Dna_list[1:]:
            CurrentProfile = CreateProfile(Motifs)
            Motifs.append(ProfileMostProbableKMer(Dna, k, CurrentProfile))
        #print(Motifs)
        if Score(Motifs) <= Score(BestMotifs):
            BestMotifs = Motifs    
        Motifs = []    
    return BestMotifs

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30305_5.txt"
    Dna, k, t = ReadInput(path)
    #print(*RandomizedMotifSearch(Dna, k, t))
    best_motifs = GreedyMotifSearch(Dna, k, t)
    print(*best_motifs)

if __name__ == main():
    main()

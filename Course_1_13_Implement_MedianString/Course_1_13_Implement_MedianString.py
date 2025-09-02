
from collections import defaultdict
from tkinter import FIRST


def ReadTextK(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k = dataset.readline()
        Dna = dataset.read()
    return Dna.strip().split(), k.strip()

def HammingDistance(p, q):
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d

def PatternTextDistance(Pattern, Text):
    return min(HammingDistance(Pattern, Text[i:i+len(Pattern)]) for i in range(len(Text) - len(Pattern) + 1))

def PatternDnaDistance(Pattern, Dna):
    return sum(PatternTextDistance(Pattern, text) for text in Dna)

def Neighbors(Pattern, d):
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return ['A', 'T', 'G', 'C']
    Neighborhood = []
    Suffix = Pattern[1:]
    SuffixNeighborhood = Neighbors(Suffix, d)
    FirstSymbol = Pattern[0]
    for i in SuffixNeighborhood:
        if HammingDistance(Suffix, i) < d:
            Neighborhood += ['A' + i, 'T' + i, 'G' + i, 'C' + i]
        else:
            Neighborhood.append(FirstSymbol + i)
    return Neighborhood 
    pass

def AllString(k):
    return Neighbors('A'*k, k)

def MedianString(Dna, k):
    d = 100000000
    Patterns = AllString(k)
    for pattern in Patterns:
        dd = PatternDnaDistance(pattern, Dna)
        if dd < d:
            Median = pattern
            d = dd
    return Median


def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30304_9 (2).txt"
    Dna, k = ReadTextK(path)
    print(Dna)
    #print(len(Neighbors('TGCAT', 2)))
    #print(*MotifEnumeration(text, int(k), int(d)))
    #print(PatternTextDistance('AAA', 'AGAG'))
    print(MedianString(Dna, int(k)))
    return 0


if __name__ == main():
    main()
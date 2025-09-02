from collections import defaultdict
from tkinter import FIRST


def ReadTextK(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k, d = dataset.readline().split()
        Dna = dataset.read()
    return Dna.strip().split(), k.strip(), d.strip()

def HammingDistance(p, q):
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d

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

def isMotif(Dna, Pattern, k, d):
    flag = False
    for i in Dna:
        for j in range(len(i)-k+1):
            if HammingDistance(Pattern, i[j:j+k]) <= d:
                flag = True
        if not flag:
            return False
        flag = False
    return True

def MotifEnumeration(Dna, k, d):
    Patterns = []
    for i in range(len(Dna)):
        for j in range(len(Dna[0])-k+1):
            #print(Neighbors(Dna[i][j:j+k], d))
            for pattern_prime in Neighbors(Dna[i][j:j+k], d):
                if isMotif(Dna, pattern_prime, k, d):
                    Patterns.append(pattern_prime)
    return list(set(Patterns))

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30302_8 (2).txt"
    text, k, d = ReadTextK(path)
    #print(k, d, text)
    #print(len(Neighbors('TGCAT', 2)))
    print(*MotifEnumeration(text, int(k), int(d)))
    return 0


if __name__ == main():
    main()
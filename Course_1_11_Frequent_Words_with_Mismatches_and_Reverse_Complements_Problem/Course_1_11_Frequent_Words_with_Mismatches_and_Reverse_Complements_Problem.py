

from collections import defaultdict
from tkinter import FIRST

def ReadTextK(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Text, k, d = dataset.readlines()
    return Text.strip(), k.strip(), d.strip()

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

def ReverseComplement(Text):
    Text = Text[::-1]
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}
    r = ""
    for i in Text:
        r += d[i]
    return r

def FrequencyTable(Text, k, d):
    freq = defaultdict(int)
    for i in range(len(Text) - k +1):
        for j in Neighbors(Text[i:i+k], d):
            freq[j] += 1
            freq[ReverseComplement(j)] += 1
    return freq

def FrequentWordsWithMismatches(Text, k, d):
    freqMap = FrequencyTable(Text, k, d)
    maxFreq = max(freqMap.values())
    frequentPatterns = []
    for pattern in freqMap.keys():
        if freqMap[pattern] == maxFreq:
            frequentPatterns.append(pattern)
    return frequentPatterns

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30278_10.txt"
    text, k, d = ReadTextK(path)
    #text, k, d = 'ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1
    print(Neighbors('CAA', 1))
    print(*FrequentWordsWithMismatches(text, int(k), int(d)))
    return 0


if __name__ == main():
    main()
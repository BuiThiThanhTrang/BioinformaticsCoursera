
from collections import defaultdict


def ReadTextPattern(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Text = dataset.readline()
        k, L, t = dataset.readline().split()
    return Text.strip(), k, L, t


def FrequencyTable(Text, k):
    freq = defaultdict(int)
    for i in range(len(Text) - k + 1):
        freq[Text[i:i+k]] += 1
    return freq


def FindClumps(Text, k, L, t):
    freqTable = FrequencyTable(Text[:L], k)
    clumps = [i for i in freqTable.keys() if freqTable[i] >= t]
    for i in range(1, len(Text) - L + 1):
        freqTable[Text[i-1:i-1+k]] -= 1
        freqTable[Text[i+L-k: i+L]] += 1
        if freqTable[Text[i+L-k: i+L]] >= t:
            clumps.append(Text[i+L-k: i+L])
    return clumps


def main():
    path = "C:\\Users\\23521\\Downloads\\E_coli.txt"
    text, k, l, t = ReadTextPattern(path)
    print(len(set(FindClumps(text, int(k), int(l), int(t)))))
    return 0


if __name__ == main():
    main()
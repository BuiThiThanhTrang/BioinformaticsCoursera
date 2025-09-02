
from collections import defaultdict

def ReadTextK(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Text, k = dataset.readlines()
    return Text.strip(), k.strip()

def FrequencyTable(Text, k):
    freq = defaultdict(int)
    for i in range(len(Text) - k +1):
        freq[Text[i:i+k]] += 1
    return freq

def FrequentWords(Text, k):
    freqMap = FrequencyTable(Text, k)
    maxFreq = max(freqMap.values())
    frequentPatterns = []
    for pattern in freqMap.keys():
        if freqMap[pattern] == maxFreq:
            frequentPatterns.append(pattern)
    return frequentPatterns

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30272_13.txt"
    text, k = ReadTextK(path)
    print(*FrequentWords(text, int(k)))
    return 0


if __name__ == main():
    main()
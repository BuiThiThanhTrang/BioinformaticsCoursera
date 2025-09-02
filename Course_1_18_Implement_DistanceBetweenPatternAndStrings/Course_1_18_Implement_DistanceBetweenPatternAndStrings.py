
def ReadTextK(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Pattern = dataset.readline()
        Dna = dataset.read()
    return Pattern.strip(), Dna.strip().split() 

def HammingDistance(p, q):
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d

def PatternTextDistance(Pattern, Text):
    return min(HammingDistance(Pattern, Text[i:i+len(Pattern)]) for i in range(len(Text) - len(Pattern) + 1))

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    return sum(PatternTextDistance(Pattern, text) for text in Dna)


def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30312_1.txt"
    Pattern, Dna = ReadTextK(path)
    print(DistanceBetweenPatternAndStrings(Pattern, Dna))
    return 0


if __name__ == main():
    main()
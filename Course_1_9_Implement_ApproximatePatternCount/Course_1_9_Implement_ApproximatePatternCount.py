

def ReadFile(path):
    with open(path, "r", encoding="utf-8") as dataset:
        pattern = dataset.readline()
        genome = dataset.readline()
        d = dataset.readline()
    return pattern.strip(), genome.strip(), int(d.strip())

def HammingDistance(p, q):
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d

def ApproximatePatternCount(pattern, genome, d):
    r= []
    l = len(pattern)
    for i in range(len(genome) - len(pattern) + 1):
        if HammingDistance(genome[i:i+l], pattern) <= d:
            r.append(i)
    return len(r)

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30278_6.txt"
    p, g, d = ReadFile(path)
    #genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
    print(ApproximatePatternCount(p, g, d))
    return 0


if __name__ == main():
    main()


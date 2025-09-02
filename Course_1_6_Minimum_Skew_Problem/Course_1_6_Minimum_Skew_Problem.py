
def ReadText(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Text = dataset.readlines()[0]
    return Text.strip()

def Skew(Genome):
    skew_diagram = [0]
    skew = 0
    for i in Genome:
        if i == 'G':
            skew += 1
        elif i == 'C':
            skew -= 1
        skew_diagram.append(skew)        
    return skew_diagram

def MinimumSkew(SkewDiagram):
    MinSkew = []
    lc = min(SkewDiagram)
    for i in range(len(SkewDiagram)):
        if SkewDiagram[i] == lc:
            MinSkew.append(i)
    return MinSkew

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30277_10.txt"
    genome = ReadText(path)
    #genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
    skew = Skew(genome)
    print(*MinimumSkew(skew))
    return 0


if __name__ == main():
    main()
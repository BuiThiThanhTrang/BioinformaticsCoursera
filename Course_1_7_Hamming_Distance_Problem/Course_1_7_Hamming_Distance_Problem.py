
def ReadFile(path):
    with open(path, "r", encoding="utf-8") as dataset:
        p = dataset.readline()
        q = dataset.readline()
    return p.strip(), q.strip()

def HammingDistance(p, q):
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30278_3.txt"
    p, q = ReadFile(path)
    #genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
    print(HammingDistance(p, q))
    return 0


if __name__ == main():
    main()

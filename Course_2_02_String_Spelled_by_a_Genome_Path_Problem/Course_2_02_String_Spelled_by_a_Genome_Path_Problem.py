
def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        GenomePath = dataset.readline().strip().split()
    return GenomePath

def Path2String(GenomePath):
    S = GenomePath[0]
    for i in range(1, len(GenomePath)):
        S += GenomePath[i][-1]
    return S

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30182_3.txt"
    GenomePath = ReadInput(path)
    print(Path2String(GenomePath))
    pass 


if __name__ == main():
    main()

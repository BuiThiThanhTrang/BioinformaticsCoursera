from collections import defaultdict

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        GenomePath = dataset.readline().strip().split()
    return GenomePath

def DeBruijn(Patterns):
    EdgeList = []
    for i in range(len(Patterns)):
        EdgeList.append([Patterns[i][:-1], Patterns[i][1:]])
    DB = defaultdict(list)
    for Node, Adj in EdgeList:
        DB[Node].append(Adj)
    return DB

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30184_8.txt"
    Patterns = ReadInput(path)
    DB = DeBruijn(Patterns)
    for key, values in DB.items():
        print(f"{key}: {' '.join(values)}")

    #The output is too long, so writing it to a file is easier for submiting
    with open("C:\\Users\\23521\\Downloads\\o.txt", "w") as f:
        for key, values in DB.items():
            f.write(f"{key}: {' '.join(values)}\n")
    pass 
    pass 


if __name__ == main():
    main()

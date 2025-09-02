from collections import defaultdict

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k = int(dataset.readline().strip())
        Text = dataset.readline().strip()
    return k, Text

def Composition(k, Text):
    Comp = []
    for i in range(len(Text) - k + 1):
        Comp.append(Text[i:i + k])
    return Comp

def DeBruijn(k, Text):
    Patterns = Composition(k - 1, Text)
    Positions = defaultdict(list)
    for i in range(len(Patterns)):
        Positions[Patterns[i]].append(i)
    DB = defaultdict(list)
    for Node, Pos in Positions.items():
        for i in Pos:
            if i + k <= len(Text):
                DB[Node].append(Text[i+1: i + k])
    return DB

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30183_6.txt"
    k, Text = ReadInput(path)
    Patterns = Composition(k - 1, Text)
    print(k)
    DB = DeBruijn(k, Text)
    for key, values in DB.items():
        print(f"{key}: {' '.join(values)}")

    #The output is too long, so writing it to a file is easier for submiting
    with open("C:\\Users\\23521\\Downloads\\o.txt", "w") as f:
        for key, values in DB.items():
            f.write(f"{key}: {' '.join(values)}\n")
    pass 


if __name__ == main():
    main()


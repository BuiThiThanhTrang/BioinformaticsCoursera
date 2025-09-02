
def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k = dataset.readline()
        Text = dataset.readline()
    return int(k.strip()), Text.strip()

def Composition(k, Text):
    Comp = []
    for i in range(len(Text) - k + 1):
        Comp.append(Text[i:i + k])
    return Comp

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30153_3.txt"
    k, Text = ReadInput(path)
    print(*Composition(k, Text))
    pass 


if __name__ == main():
    main()
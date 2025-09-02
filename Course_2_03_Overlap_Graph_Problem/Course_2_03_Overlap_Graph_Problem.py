from collections import defaultdict

class OverlapGraph:
    def __init__(self, Patterns):
        self.Nodelist = list(set(Patterns))
        self.NumNodes = len(self.Nodelist)
        self.AdjacencyList = defaultdict(list)
        for i in range(self.NumNodes):
            for j in range(self.NumNodes):
                if self.Nodelist[i][1:] == self.Nodelist[j][:-1]:
                    self.AdjacencyList[self.Nodelist[i]].append(self.Nodelist[j])
        pass

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Patterns = dataset.readline().strip().split()
    return Patterns

def Path2String(GenomePath):
    S = GenomePath[0]
    for i in range(1, len(GenomePath)):
        S += GenomePath[i][-1]
    return S

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30182_10.txt"
    Patterns = ReadInput(path)
    OG = OverlapGraph(Patterns)
    for key, values in OG.AdjacencyList.items():
        print(f"{key}: {' '.join(values)}")

    #The output is too long, so writing it to a file is easier for submiting
    #with open("C:\\Users\\23521\\Downloads\\o.txt", "w") as f:
        #for key, values in OG.AdjacencyList.items():
            #f.write(f"{key}: {' '.join(values)}\n")
    pass 


if __name__ == main():
    main()


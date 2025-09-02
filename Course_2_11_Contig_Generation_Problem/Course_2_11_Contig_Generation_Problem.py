from collections import defaultdict
import copy
import random
from itertools import chain


class GenomeGraph:
    def __init__(self, AdjacenyList):
        self.AdjacenyList = AdjacenyList
        self.Out = defaultdict(int)
        self.In = defaultdict(int)
        for Node in AdjacenyList:
            self.Out[Node] = len(self.AdjacenyList[Node])
        for Node in AdjacenyList:
            for i in AdjacenyList[Node]:
                self.In[i] += 1
    
    def getNodes(self):
        keys = list(self.AdjacenyList.keys())
        values = list(chain.from_iterable(self.AdjacenyList.values()))
        return list(set(keys + values))
        pass

    def MaximalNonBranchingPaths(self):
        Paths = []
        OutCopy = copy.deepcopy(self.Out)
        InCopy = copy.deepcopy(self.In)
        AdjList = copy.deepcopy(self.AdjacenyList)
        # Get node list
        NodeList = self.getNodes()
        Visited = {}
        for Node in NodeList:
            Visited[Node] = False
        for Node in NodeList:
            if not (InCopy[Node] == 1 and OutCopy[Node] == 1):
                if OutCopy[Node] > 0:
                    Visited[Node] = True
                    for Adj in AdjList[Node]:
                        Visited[Adj] = True
                        NonBranchingPath = [Node, Adj]
                        w = Adj
                        while InCopy[w] == 1 and OutCopy[w] == 1:
                            w = AdjList[w][0]
                            Visited[w] = True
                            NonBranchingPath.append(w)
                        Paths.append(NonBranchingPath)

        #print(Visited)
        for Node in NodeList:
            if Visited[Node] == False and (InCopy[Node] == 1 and OutCopy[Node] == 1):
                Visited[Node] = True
                NonBranchingPath = [Node, AdjList[Node][0]]
                w = AdjList[Node][0]
                while w != Node:
                    Visited[w] = True
                    w = AdjList[w][0]
                    NonBranchingPath.append(w)
                Paths.append(NonBranchingPath)
        return Paths

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Patterns = dataset.readline().strip().split()
    return Patterns

def DeBruijn(Patterns):
    EdgeList = []
    for i in range(len(Patterns)):
        EdgeList.append([Patterns[i][:-1], Patterns[i][1:]])
    DB = defaultdict(list)
    for Node, Adj in EdgeList:
        DB[Node].append(Adj)
    return DB

def Path2String(GenomePath):
    S = GenomePath[0]
    for i in range(1, len(GenomePath)):
        S += GenomePath[i][-1]
    return S

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30189_5.txt"
    Patterns = ReadInput(path)
    DB = DeBruijn(Patterns)

    Graph = GenomeGraph(DB)
    Paths = Graph.MaximalNonBranchingPaths()
    r = []
    for i in Paths:
        r.append(Path2String(i))
    print(' '.join(r))

    #The output is too long, so writing it to a file is easier for submiting
    with open("C:\\Users\\23521\\Downloads\\o.txt", "w") as f:
        f.write(' '.join(r))
    pass 
    pass 


if __name__ == main():
    main()

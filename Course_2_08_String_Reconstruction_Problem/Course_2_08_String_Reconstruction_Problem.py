from collections import defaultdict
import copy
import sys
sys.setrecursionlimit(3000)  # Be cautious with very large values

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

    def EulerianCycle(self, start = '0'):
        Path = []
        OutCopy = self.Out
        AdjList = self.AdjacenyList
        # Find unbalances node
        for Node in self.AdjacenyList:
            if self.Out[Node] - self.In[Node] == 1:
                start = Node 
        # Find Eulerian Path using Hierholzer's algorithm
        #def DFS(at):
        #    while OutCopy[at] != 0:
        #        Next = AdjList[at].pop(0)
        #        OutCopy[at] -= 1
        #        DFS(Next)
        #        pass
        #    Path.insert(0, at)
        #
        #DFS(start)
        stack = [start]

        while stack:
            current = stack[-1]
            if OutCopy[current] > 0:
                next_node = AdjList[current].pop(0)
                OutCopy[current] -= 1
                stack.append(next_node)
            else:
                Path.insert(0, stack.pop())
        return Path

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k = int(dataset.readline().strip())
        Patterns = dataset.readline().strip().split()
    return k, Patterns

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
    path = "C:\\Users\\23521\\Downloads\\dataset_30187_7.txt"
    k, Patterns = ReadInput(path)
    DB = DeBruijn(Patterns)
    #print(DB)
    Graph = GenomeGraph(DB)
    GenomePath = Graph.EulerianCycle()
    #print(GenomePath)
    print(Path2String(GenomePath))
    #print(*Graph.EulerianCycle())
    #print(Graph.AdjacenyList)
    #with open("C:\\Users\\23521\\Downloads\\o.txt", "w") as f:
    #    f.write(Path2String(GenomePath))

if __name__ == main():
    main()


from collections import defaultdict
import copy

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
        OutCopy = copy.deepcopy(self.Out) 
        AdjList = copy.deepcopy(self.AdjacenyList)
        # Find unbalances node
        for Node in self.AdjacenyList:
            if self.Out[Node] - self.In[Node] == 1:
                start = Node 
        # Find Eulerian Path using Hierholzer's algorithm
        def DFS(at):
            while OutCopy[at] != 0:
                Next = AdjList[at].pop(0)
                OutCopy[at] -= 1
                DFS(Next)
                pass
            Path.insert(0, at)

        DFS(start)
        return Path

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        Text = dataset.read().strip().split('\n')

    AdjList = {}
    for Node in Text:
        current, neighbors = Node.split(': ')
        AdjList[current] = neighbors.split()
    return AdjList

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30187_6.txt"
    AdjList = ReadInput(path)
    #print(AdjList)
    Graph = GenomeGraph(AdjList)
    print(*Graph.EulerianCycle())
    #print(Graph.AdjacenyList)

if __name__ == main():
    main()

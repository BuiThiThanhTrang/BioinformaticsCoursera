from collections import defaultdict
import copy
import random

class GenomeGraph:
    def __init__(self, AdjacenyList, k, d):
        self.AdjacenyList = AdjacenyList
        self.k = k
        self.d = d
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

        #--No recursion--
        # Find an abitrary Eulerian Path
        stack = [start]
        while stack:
            current = stack[-1]
            if OutCopy[current] > 0:
                idx = random.randint(0, len(AdjList[current]) - 1)
                next_node = AdjList[current].pop()
                OutCopy[current] -= 1
                stack.append(next_node)
            else:
                Path.insert(0, stack.pop())
        # Randomly create eulerian paths until get a legal one
        while not isValidPath(self.k, self.d, Path):
            stack = [start]
            Path = []
            OutCopy = copy.deepcopy(self.Out)
            AdjList = copy.deepcopy(self.AdjacenyList)
            while stack:
                current = stack[-1]
                if OutCopy[current] > 0:
                    idx = random.randint(0, len(AdjList[current]) - 1)
                    next_node = AdjList[current].pop()
                    OutCopy[current] -= 1
                    stack.append(next_node)
                else:
                    Path.insert(0, stack.pop())
        return Path



def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k, d = dataset.readline().strip().split()
        k = int(k) 
        d = int(d)
        Pairs = dataset.readline().strip().split()
        Pairs = [i.split('|') for i in Pairs]
    return k, d, Pairs

def DeBruijn(Pairs):
    EdgeList = []
    for i in range(len(Pairs)):
        EdgeList.append([(Pairs[i][0][:-1], Pairs[i][1][:-1]), (Pairs[i][0][1:], Pairs[i][1][1:])])
    DB = defaultdict(list)
    for Node, Adj in EdgeList:
        DB[Node].append(Adj)
    return DB

def isValidPath(k, d, Path):
    k = k - 1
    d = d + 1 
    s = Path[0][0] + ' ' * d + Path[0][1]
    s = list(s)
    for i in range(1, len(Path)):
        CurrentNode = Path[i][0] + ' ' * d + Path[i][1]
        CurrentNode = list(CurrentNode)
        for j in range(i, len(s)):
            if s[j] == ' ':
                s[j] = CurrentNode[j - i]
            elif CurrentNode[j - i] != ' ' and s[j] != CurrentNode[j - i]:
                return False
        s += CurrentNode[-1]

    return s


def Path2String(GenomePath):
    S = GenomePath[0]
    for i in range(1, len(GenomePath)):
        S += GenomePath[i][-1]
    return S

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30188_16 (1).txt"
    k, d, Pairs = ReadInput(path)
    #print(Pairs)
    DB = DeBruijn(Pairs)
    #print(DB)
    Graph = GenomeGraph(DB, k, d)
    GenomePath = Graph.EulerianCycle()
    print(GenomePath)
    #print(''.join(isValidPath(k, d, GenomePath)))
    #print(Path2String(GenomePath))
    #print(*Graph.EulerianCycle())
    #print(Graph.AdjacenyList)
    with open("C:\\Users\\23521\\Downloads\\o.txt", "w") as f:
        f.write(''.join(isValidPath(k, d, GenomePath)))

if __name__ == main():
    main()


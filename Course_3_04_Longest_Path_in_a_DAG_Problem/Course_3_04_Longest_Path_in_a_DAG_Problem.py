import copy
import numpy as np
from collections import defaultdict
import sys

sys.setrecursionlimit(2000)


def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        source, sink = dataset.readline().strip().split()
        source = int(source)
        sink = int(sink)

        Predecessors = defaultdict(list)
        for line in dataset.readlines():
            edge_start, edge_end, weight = [int(i) for i in line.split()]
            Predecessors[edge_end].append((edge_start, weight))

    return source, sink, Predecessors

def DAGLongestPathBackTrack(source, sink, Predecessors):
    s = defaultdict(int)
    Backtrack = defaultdict(int)
    s[source] = 0
    Backtrack[source] = 0
    topo_nodes = list(Predecessors.keys())
    topo_nodes.sort()
    for node in topo_nodes:
        longest_path = 0
        for predecessor, weight in Predecessors[node]:
            if s[predecessor] + weight > longest_path:
                longest_path  = s[predecessor] + weight
                Backtrack[node] = predecessor
        s[node] = longest_path
    
    return s, Backtrack

def OutputDAGLongestPath(source, sink, s, Backtrack):
    path = []
    end = sink
    while end != source:
        path.insert(0, end)
        end = Backtrack[end]
    path.insert(0, end)
    return s[sink], path

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30197_7.txt"
    source, sink, Predecessors = ReadInput(path)
    print(Predecessors)
    s, Backtrack = DAGLongestPathBackTrack(source, sink, Predecessors)
    print(s, Backtrack)
    longest_path_len, longest_path = OutputDAGLongestPath(source, sink, s, Backtrack)
    print(longest_path_len)
    print(*longest_path)



if __name__ == main():
    main()
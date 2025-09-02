from collections import defaultdict
import copy
import random

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        k, d = dataset.readline().strip().split()
        k = int(k) 
        d = int(d)
        Pairs = dataset.readline().strip().split()
        Pairs = [i.split('|') for i in Pairs]
    return k, d, Pairs

def StringSpelledByPatterns(k, d, Path):
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


def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30208_4.txt"
    k, d, GenomePath = ReadInput(path)
    #print(GenomePath)
    print(''.join(StringSpelledByPatterns(k, d, GenomePath)))
    #with open("C:\\Users\\23521\\Downloads\\o.txt", "w") as f:
        #f.write(''.join(isValidPath(k, d, GenomePath)))

if __name__ == main():
    main()

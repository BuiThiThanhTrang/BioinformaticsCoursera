import copy
import numpy as np
import sys

sys.setrecursionlimit(2000)


def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        s, t = dataset.readlines()

    return s.strip(), t.strip()


def LCSBackTrack(v, w):
    # 1:down, 2:right, 3:diagonal
    n = len(v) + 1
    m = len(w) + 1
    Backtrack = np.zeros((n, m), dtype=int)
    s = np.zeros((n, m), dtype=int)
    for i in range(1, n):
        for j in range(1, m):
            match = 0
            if v[i - 1] == w[j - 1]:
                match = 1
            s[i, j] = max(s[i - 1, j], s[i, j-1], s[i - 1, j - 1] + match)
            if s[i, j] == s[i - 1, j]:
                Backtrack[i, j] = 1
            elif s[i, j] == s[i, j - 1]:
                Backtrack[i, j] = 2
            elif s[i, j] == s[i - 1, j - 1] + match:
                Backtrack[i, j] = 3
    return Backtrack


def OutputLCS(backtrack, v, i, j):
    # 1:down, 2:right, 3:diagonal
    if i == 0 or j == 0:
        return ""
    if backtrack[i,j] == 1:
        return OutputLCS(backtrack, v, i-1, j)
    if backtrack[i,j] == 2:
        return OutputLCS(backtrack, v, i, j-1)
    if backtrack[i,j] == 3:
        return OutputLCS(backtrack, v, i-1, j-1) + v[i-1]




def main():
    path = "C:\\Users\\23521\\Downloads\\i.txt"
    s, t = ReadInput(path)
    backtrack = LCSBackTrack(s, t)
    print(s, "\n\n", t)
    print(LCSBackTrack(s, t))
    print()
    print(OutputLCS(backtrack, s, len(s), len(t)))



if __name__ == main():
    main()

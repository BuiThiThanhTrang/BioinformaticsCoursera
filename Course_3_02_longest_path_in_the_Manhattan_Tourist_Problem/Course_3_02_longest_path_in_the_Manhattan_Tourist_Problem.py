import copy
import numpy as np

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        n, m = dataset.readline().strip().split()
        n = int(n)
        m = int(m)

        DownStr = []
        for i in range(n):
            DownStr.append(dataset.readline().strip().split())
        Down = np.asmatrix(DownStr, dtype = int)
        Down = np.vstack([np.zeros((1, Down.shape[1]), dtype=int), Down])
        dataset.readline()

        RightStr = []
        for i in range(n+1):
            RightStr.append(dataset.readline().strip().split())
        Right = np.asmatrix(RightStr, dtype = int)
        Right = np.hstack([np.zeros((Right.shape[0], 1), dtype=int), Right])

    return n, m, Down, Right


def ManhattanTourist(n, m, Down, Right):
    s = np.zeros((n+1, m+1), dtype=int)
    for i in range(1,n+1):
        s[i,0] = Down[i,0] + s[i-1,0]

    for i in range(1,m+1):
        s[0,i] = Right[0,i] + s[0,i-1]

    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i,j] = max(s[i, j-1] +Right[i,j], s[i-1,j] + Down[i,j])

    return s[n,m]

def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30205_10.txt"
    n, m, Down, Right = ReadInput(path)
    print(n, m, Down, Right)
    print(ManhattanTourist(n, m, Down, Right))





if __name__ == main():
    main()
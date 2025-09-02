import copy

def ReadInput(path):
    with open(path, "r", encoding="utf-8") as dataset:
        money = int(dataset.readline().strip())
        Coins = dataset.readline().strip().split()
        Coins = [int(i) for i in Coins]
    return money, Coins

# traditional approach
# def DPChange(money, Coins):
#     DP = [0]*(money+1)
#     for i in range(1, money+1):
#         DP[i] = min([DP[max(0, i-coin)] for coin in Coins])+1
#     print(DP)
#     return DP[money]

# DP length = max(Coins)
# def DPChange(money, Coins):
#     l = Coins[0] + 1
#     DP = [0]*(l)
#     for i in range(1, money+1):
#         DP[i % l] = min([DP[max(0, (i-coin)) % l] for coin in Coins])+1
#     return DP[money % l]

def DPChange(money, Coins):
    l = Coins[0] + 1
    DP = {i:[0, []] for i in range(Coins[0]+1)}

    for i in range(1, money+1):
    #     DP[i % l] = min([DP[max(0, (i-coin)) % l] for coin in Coins])+1
        MinCoinsPos = max(0, (i-Coins[-1])) % l  
        ChooseCoin = 0
        for coin in Coins:
            if coin <= i:
                if DP[(i-coin) % l][0] <= DP[MinCoinsPos][0]:
                    MinCoinsPos = max(0, (i-coin)) % l 
                    ChooseCoin = coin
                    # print(ChooseCoin)
        
        DP[i % l][0] = DP[MinCoinsPos][0] +1
        DP[i % l][1] = copy.deepcopy(DP[MinCoinsPos][1]) + [ChooseCoin]
    print(DP)
    
    return DP[money % l]


def main():
    path = "C:\\Users\\23521\\Downloads\\dataset_30195_10 (1).txt"
    money, Coins = ReadInput(path)

    # print(-1 % 5)
    print(DPChange(money, Coins))


if __name__ == main():
    main()
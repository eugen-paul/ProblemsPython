import math


for _ in range(int(input())):
    n = int(input())
    best = -1
    bestA = math.inf
    bestB = math.inf
    bestAB = math.inf
    for _ in range(n):
        m, s = input().split(" ")
        if s == "00":
            continue
        if s == "10":
            bestA = min(int(m), bestA)
        elif s == "01":
            bestB = min(int(m), bestB)
        else:
            bestAB = min(int(m), bestAB)
    best = min(bestAB, bestA+bestB)
    if best == math.inf:
        print(-1)
    else:
        print(best)

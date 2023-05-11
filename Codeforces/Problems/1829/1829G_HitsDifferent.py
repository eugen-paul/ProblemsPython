from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


dp = [0] * (2023*2024//2 + 1)
dp[1] = 1
line = 2
line_size = 2
pos = 1

for _ in range(int(input())):
    n = int(input())

    while pos < n:
        x = 0
        for i in range(pos, pos + line_size):
            if x == 0:
                dp[i+1] = (i+1)**2 + dp[i+1-(line_size-1)]
            elif x == line_size-1:
                dp[i+1] = (i+1)**2 + dp[i+1-line_size]
            else:
                dp[i+1] = (i+1)**2 + dp[i+1-(line_size-1)] + dp[i+1-line_size] - dp[i+1-(line_size-1)-(line_size-1)]
            x += 1
        pos += line_size
        line_size += 1

    print(dp[n])

# internet solution
# t = int(input())
# obr = [n * (n + 1) // 2 for n in range(2024)]
# for tt in range(t):
#     n = int(input())
#     i = 0
#     while obr[i] < n:
#         i += 1
#     l = obr[i] + 1 - n
#     r = n - obr[i - 1]
#     res = 0
#     for i in range(l):
#         for j in range(1, r + 1):
#             res += (obr[j + i] - i) ** 2
#     print(res)

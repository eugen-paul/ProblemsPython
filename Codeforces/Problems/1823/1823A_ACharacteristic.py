from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import sys
input = sys.stdin.readline


def i_array_int() -> List[int]:
    return list(map(int, input().split()))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split())) for _ in range(h)]


MOD = 10**9+7


def inv(x):
    return pow(x % MOD, MOD - 2, MOD)


s = [0]
for i in range(101):
    s.append(s[-1] + i)

for _ in range(int(input())):
    n, k = i_array_int()
    ok = False
    for i in range(n, -1, -1):
        if s[i] + s[n-i] == k:
            print("YES")
            ans = [1] * i + [-1] * (n-i)
            print(" ".join(str(x) for x in ans))
            ok = True
            break

    if not ok:
        print("NO")

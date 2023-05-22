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


for _ in range(int(input())):
    n, k = i_array_int()
    p = i_array_int()

    ok = True
    errs = 0
    for i, c in enumerate(p):
        if abs((i+1) - c) % k != 0:
            ok = False
            errs += 1
    if ok:
        print(0)
    elif errs == 2:
        print(1)
    else:
        print(-1)

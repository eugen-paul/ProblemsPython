from collections import defaultdict
from itertools import permutations
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


MOD = 10**9+7
for _ in range(int(input())):
    n = int(input())
    a = i_array_int()
    a.sort()
    b = i_array_int()
    b.sort()

    p1, p2 = 0, 0

    resp = 1

    while p2 < len(b):
        while p1 < len(a) and a[p1] <= b[p2]:
            p1 += 1
        if p1 > p2:
            resp = 0
            break
        resp = resp * (p2-p1+1) % MOD
        p2 += 1

    print(resp)

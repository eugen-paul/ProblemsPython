from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    n, k = i_array_int()
    a = i_array_int()
    a.sort()
    cur = sum(a[:len(a)-k:])
    best = cur
    for i in range(k):
        cur -= a[2*i] + a[2*i+1]
        cur += a[len(a)-k+i]
        best = max(best, cur)
    print(best)

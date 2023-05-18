from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import sys
input = sys.stdin.readline


def i_array_int() -> List[int]:
    return list(map(int, input().split()))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split())) for _ in range(h)]


for _ in range(int(input())):
    n, t = i_array_int()
    a = i_array_int()
    b = i_array_int()

    best = 0
    ans = -1
    for i, n in enumerate(a):
        tt = n+i
        if tt <= t and b[i] > best:
            ans = i+1
            best = b[i]
    print(ans)

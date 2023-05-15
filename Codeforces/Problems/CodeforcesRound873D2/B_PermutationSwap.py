from collections import defaultdict
from math import inf, gcd
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    n = int(input())
    a = i_array_int()
    d = []
    for i, n in enumerate(a):
        if i+1 == n:
            continue
        d.append(abs(i+1 - n))
    print(gcd(*d))

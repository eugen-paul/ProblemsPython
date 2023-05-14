from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


for _ in range(int(input())):
    n = int(input())
    a = i_array_int()
    d = []
    for i, n in enumerate(a):
        if i+1 == n:
            continue
        d.append(abs(i+1 - n))
    resp = 0
    for n in d:
        if resp == 0:
            resp = n
        else:
            resp = gcd(n, resp)
    print(resp)

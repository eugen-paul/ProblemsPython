from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


def comp(n, m, a) -> int:
    resp = 0
    if n < m:
        n, m = m, n
    if m > 1:
        resp += abs(a[-1] - a[1]) * (m-1)
    if n > 1:
        resp += abs(a[-1] - a[0]) * (n-1) * (m)
    return resp


for _ in range(int(input())):
    n, m = i_array_int()
    a = i_array_int()
    a.sort()
    resp = comp(n, m, a)
    a = a[::-1]
    resp = max(resp, comp(n, m, a))
    print(resp)

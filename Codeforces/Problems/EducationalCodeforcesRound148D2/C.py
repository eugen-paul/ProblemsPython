from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    n = int(input())
    a = i_array_int()
    c = 0
    last = a[0]

    for i in range(1, len(a)-1):
        if last <= a[i] and a[i] <= a[i+1]:
            c += 1
        elif last >= a[i] and a[i] >= a[i+1]:
            c += 1
        else:
            last = a[i]

    resp = len(a) - c
    if resp == 2 and a[0] == a[-1]:
        print(1)
    else:
        print(resp)

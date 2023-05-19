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
    n, k = i_array_int()
    a = i_array_int()
    b = i_array_int()

    a = [(i, x) for i, x in enumerate(a)]

    a.sort(key=lambda x: x[1])
    b.sort()
    b = [(i, x) for i, x in enumerate(b)]
    b.sort(key=lambda x: a[x[0]][0])

    print(" ".join(str(x) for _, x in b))

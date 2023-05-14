from collections import defaultdict
from math import ceil, gcd, inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    n = int(input())
    a = [i for i in range(1, n+1)]
    s = sum(a)
    r = ceil(s / n)
    a[0] = r * n - s + 1

    print(" ".join([str(x) for x in a]))

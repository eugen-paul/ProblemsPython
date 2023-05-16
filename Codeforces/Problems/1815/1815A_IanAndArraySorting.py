from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    n = int(input())
    ar = i_array_int()

    even = sum(ar[::2])
    odd = sum(ar[1::2])

    if n & 1 == 1 or odd >= even:
        print("YES")
    else:
        print("NO")

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
    n = int(input())
    a = i_array_int()
    even = [x for x in a if x & 1 == 0]
    odd = [x for x in a if x & 1 == 1]

    if len(even) == 0 or len(odd) == 0:
        print("YES")
        continue

    min_even = min(even)
    min_odd = min(odd)

    if min_odd < min_even:
        print("YES")
        continue

    print("NO")

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
    a = input()[:-1]
    s = set()
    for i in range(len(a)-1):
        s.add(a[i:i+2])
    print(len(s))

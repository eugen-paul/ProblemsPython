from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import sys
input = sys.stdin.readline


def i_array_int() -> List[int]:
    return list(map(int, input().split()))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split())) for _ in range(h)]


MOD = 10**9+7


def inv(x):
    return pow(x % MOD, MOD - 2, MOD)


for _ in range(int(input())):
    n = int(input())
    a = input()[:-1]

    g = max((map(len, a.split(">"))))
    s = max((map(len, a.split("<"))))
    print(max(s+1, g+1))

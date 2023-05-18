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

    ans = n * 4

    l = n-1
    ll = n-1-1
    a = l*(l+1) // 2
    b = ll*(ll+1) // 2
    ans += a+b+1

    print(ans)

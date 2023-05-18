import math
from collections import defaultdict
from math import gcd, inf
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

    ans = 0
    for i in range(n//2):
        ans = gcd(ans, abs(a[i] - a[n-1-i]))
    print(ans)

test = False
if test:
    # v2
    for _ in range(int(input())):
        n = int(input())
        a = i_array_int()

        ans = -1
        for i in range(n//2):
            f, l = a[i], a[n-1-i]
            if f == l:
                continue
            if ans == -1:
                ans = abs(f-l)
            else:
                ans = gcd(ans, abs(f-l))
        if ans >= 0:
            print(ans)
        else:
            print(0)
    # v1
    for _ in range(int(input())):
        n = int(input())
        a = i_array_int()

        g = []
        for i in range(n//2):
            f, l = a[i], a[n-1-i]
            if f == l:
                continue
            dis = abs(f-l)
            g.append(dis)
        if len(g) > 0:
            print(gcd(*g))
        else:
            print(0)

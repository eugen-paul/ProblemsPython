import bisect
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


def mul(a, b):
    return a * b % MOD


def inv(x):
    return pow(x % MOD, MOD - 2, MOD)


# for _ in range(int(input())):
#     n, m = i_array_int()
#     a = sorted(i_array_int())

#     c = []
#     u = []
#     cur = -1
#     for i in a:
#         if cur != i:
#             c.append(1)
#             u.append(i)
#             cur = i
#         else:
#             c[-1] += 1

#     mults = [1] * (len(c) + 1)
#     for i in range(len(c)):
#         mults[i+1] = mul(mults[i], c[i])

#     resp = 0
#     for start in range(len(u) - m + 1):
#         if u[start + m - 1] == u[start] + m - 1:
#             resp += mults[start + m] * inv(mults[start]) % MOD

#     print(resp % MOD)


for _ in range(int(input())):
    n, m = i_array_int()
    a = sorted(i_array_int())

    c = Counter(a)  # counter are to slow on not sorted list => sort a
    u = list(set(a))
    u.sort()

    mult = 1
    for pos in range(min(len(u), m-1)):
        mult = mult * c[u[pos]] % MOD

    resp = 0
    for start in range(len(u) - m + 1):
        mult = mult * c[u[start + m - 1]] % MOD
        if u[start + m - 1] == u[start] + m - 1:
            resp += mult % MOD
        mult = mult * pow(c[u[start]] % MOD, MOD - 2, MOD)

    print(resp % MOD)

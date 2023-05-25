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
    s = input()[:-1]
    if s.count("(") != s.count(")"):
        print(-1)
        continue

    rev = s[::-1]
    v = 0
    for c in rev:
        if c == "(":
            v += 1
        else:
            v -= 1
        if v < 0:
            break
    if v == 0:
        print(1)
        print(" ".join("1" for _ in rev))
        continue

    resp = [2] * len(s)
    r = 0
    for l in range(len(s)):
        if s[l] == "(":
            pos = -1
            for p in range(max(r, l)+1, len(s)):
                if s[p] == ")":
                    pos = p
                    break
            r = p
            if pos != -1:
                resp[l] = 1
                resp[pos] = 1

    cnt_1 = 1 if resp.count(1) > 0 else 0
    cnt_2 = 1 if resp.count(2) > 0 else 0
    cnt = cnt_1 + cnt_2
    print(cnt)
    if cnt == 2:
        print(*resp)
    else:
        print(" ".join("1" for _ in resp))

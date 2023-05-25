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
    s = list(input()[:-1])
    if s.count("?") == 0:
        print("".join(str(x) for x in s))
        continue

    l = "1"
    cnt = 0
    for i in range(len(s)):
        if s[i] == "?":
            cnt += 1
        elif cnt > 0:
            if s[i] == "1" and l == "1":
                s[i-cnt:i] = [1] * cnt
                cnt = 0
            else:
                s[i-cnt:i] = [0] * cnt
                cnt = 0
            l = s[i]
        else:
            l = s[i]

    if cnt > 0:
        if l == "1":
            s[-cnt:len(s)] = [1] * cnt
        else:
            s[-cnt:len(s)] = [0] * cnt

    print("".join(str(x) for x in s))

from collections import defaultdict
from math import ceil, inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import sys
input = sys.stdin.readline


def i_array_int() -> List[int]:
    return list(map(int, input().split()))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split())) for _ in range(h)]


for _ in range(int(input())):
    n = int(input())
    s = input()[:-1]
    if len(s) & 1 == 1:
        print(-1)
        continue

    chars = Counter(s)
    if chars.most_common(1)[0][1] * 2 > n:
        print(-1)
        continue

    pairs = Counter()
    for i in range(len(s)//2):
        if s[i] == s[- 1 - i]:
            pairs[s[i]] += 1

    if len(pairs) > 0:
        print(max(ceil(sum(pairs.values()) / 2), pairs.most_common(1)[0][1]))
    else:
        print(0)

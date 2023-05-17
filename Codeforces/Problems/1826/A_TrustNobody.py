from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    n = int(input())
    l = i_array_int()
    c = Counter(l)

    s = []
    for i, v in c.items():
        s.append((i, v))
    s.sort()

    ans = -1
    cnt = 0
    for i, v in s:
        cnt += v
        rest = n-cnt
        if rest >= i:
            ans = rest
        elif ans >= i:
            ans = -1
            break
        else:
            break

    print(ans)

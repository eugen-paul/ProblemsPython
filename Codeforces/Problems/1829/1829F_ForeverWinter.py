from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    n, m = i_array_int()

    c = Counter()
    for _ in range(m):
        a, b = i_array_int()
        c[a] += 1
        c[b] += 1

    c2 = Counter()
    for _, v in c.items():
        if v != 1:
            c2[v] += 1

    if len(c2) == 2:
        print(c2.most_common(2)[1][0], c2.most_common(1)[0][0]-1)
    else:
        print(c2.most_common(1)[0][0], c2.most_common(1)[0][0]-1)

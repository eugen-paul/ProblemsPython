from collections import defaultdict
from math import inf, ceil, floor, sqrt
import math
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    s = input()

    resp = inf
    for i in range(26):
        c = chr(i + ord('a'))
        p = max(map(len, s.split(c)))
        resp = min(resp, ceil(math.log2(p+1)))

    print(resp)

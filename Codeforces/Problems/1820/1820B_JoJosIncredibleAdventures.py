from collections import defaultdict
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    s = list(map(len, input().split("0")))
    if len(s) == 0:
        print(0)
        continue
    if len(s) == 1:
        print(s[0]**2)
        continue
    s[-1] = s[-1] + s[0]
    m = max(s)
    print(math.ceil((m+1)/2) * math.floor((m+1)/2))

# for s in [*open(0)][1:]:
#     print((max(map(len, (s[:-1]+s[:-2]).split('0')))+1)**2//4)

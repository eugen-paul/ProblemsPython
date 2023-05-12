from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    s = input()
    c = Counter(s)
    if len(c) == 1:
        print("NO")
        continue
    if len(c) > 2:
        print("YES")
        continue
    if c.most_common(2)[1][1] == 1:
        print("NO")
    else:
        print("YES")
    

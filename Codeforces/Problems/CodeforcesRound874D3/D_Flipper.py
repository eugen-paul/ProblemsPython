from collections import defaultdict
from math import inf
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
    if len(a) == 1:
        print(a[0])
        continue

    b = {x: i for i, x in enumerate(a)}

    max_pos = b[len(a)]
    max_pos2 = b[len(a)-1]

    # target array must start with max value (n) or with second max value (n-1) if n ist on position 0
    if max_pos == 0:
        max_pos = max_pos2

    # Cases:
    # 1. a[max_pos:] is the third part
    # 2. a[max]      is the second part if a[max] ist last element
    # 3. a[::-1]     if a[max] ist last element (this case with covered with the case one)
    v1 = [0] * max_pos

    # check 2.
    if max_pos == len(a) - 1:
        v1 = [a[-1]] + a[:len(a)-1:]

    # check 1. and 3.
    check = [0] * max_pos
    for i in range(max_pos):
        tmp = a[i:max_pos][::-1] + a[:i]
        check = max(check, tmp)

    check = a[max_pos:]+check

    check = max(check, v1)

    print(" ".join(str(x) for x in check))


# toslow
test = False
if test:
    for _ in range(int(input())):
        n = int(input())
        a = i_array_int()

        check = [0] * len(a)

        for start in range(len(a)):
            for l in range(1, len(a) - start + 1):
                end = start+l
                a1, a2, a3 = a[end:], a[start: end][::-1], a[:start]
                tmp = a[end:] + a[start: end][::-1] + a[:start]
                check = max(check, tmp)
        print(" ".join(str(x) for x in check))

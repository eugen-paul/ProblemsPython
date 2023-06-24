from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        resp = 0

        resp = min(x, y)*2 + z

        if x != y:
            resp += 1

        return resp * 2


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.longestString(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, 5, 1, 12)
    do_test(1, 3, 2, 2, 14)
    do_test(2, 1, 1, 2, 8)
    do_test(3, 0, 0, 2, 4)
    do_test(4, 0, 1, 7, 16)
    do_test(5, 0, 0, 0, 0)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

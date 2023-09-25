from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)
        c3 = c2 - c1
        resp = ""
        for k, v in c3.items():
            resp += v*k
        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findTheDifference(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "abcd", "abcde", "e")
    do_test(1, "", "y", "y")
    do_test(2, "y", "y", "")


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

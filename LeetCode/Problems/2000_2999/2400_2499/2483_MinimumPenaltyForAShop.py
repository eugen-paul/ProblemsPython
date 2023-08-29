from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur = customers.count("N")
        resp = cur
        time = len(customers)
        for i, c in enumerate(reversed(customers)):
            if c == "Y":
                cur += 1
            else:
                cur -= 1
            if resp >= cur:
                resp = cur
                time = len(customers) - i - 1

        return time


def do_test(i: int, s, r):
    c = Solution()
    resp = c.bestClosingTime(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "YYNY", 2)
    do_test(1, "NNNNN", 0)
    do_test(2, "YYYY", 4)


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

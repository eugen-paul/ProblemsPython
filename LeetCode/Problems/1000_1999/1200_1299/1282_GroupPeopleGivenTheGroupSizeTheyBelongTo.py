from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        m: Dict[int, List[int]] = defaultdict(list)
        resp = []

        for i, n in enumerate(groupSizes):
            m[n].append(i)
            if len(m[n]) == n:
                resp.append(m[n])
                m[n] = list()

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.groupThePeople(s)
    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 3, 3, 3, 3, 1, 3], [[5], [0, 1, 2], [3, 4, 6]])
    do_test(1, [2, 1, 3, 3, 3, 2], [[1], [0, 5], [2, 3, 4]])


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

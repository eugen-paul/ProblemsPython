from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        grid = set()
        for x, y in coordinates:
            grid.add((x, y))

        resp = [(m-1)*(n-1), 0, 0, 0, 0]
        SEEN = set()

        def check(x, y):
            if (x, y) in SEEN:
                return

            resp[0] -= 1

            cnt = 0
            if (x, y) in grid:
                cnt += 1
            if (x+1, y) in grid:
                cnt += 1
            if (x+1, y+1) in grid:
                cnt += 1
            if (x, y+1) in grid:
                cnt += 1
            resp[cnt] += 1

            SEEN.add((x, y))

        for x, y in grid:
            if x > 0 and y > 0:
                check(x-1, y-1)
            if x > 0 and y < n-1:
                check(x-1, y)
            if x < m-1 and y > 0:
                check(x, y-1)
            if x < m-1 and y < n - 1:
                check(x, y)

        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.countBlackBlocks(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 3,  [[0, 0]], [3, 1, 0, 0, 0])
    do_test(1, 3, 3,  [[0, 0], [1, 1], [0, 2]], [0, 2, 2, 0, 0])
    do_test(2, 2, 3,  [[0, 0], [1, 1]], [0, 1, 1, 0, 0])

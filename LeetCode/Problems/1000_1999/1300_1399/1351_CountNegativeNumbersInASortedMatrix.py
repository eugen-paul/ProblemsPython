import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        resp = 0

        n = len(grid)
        m = len(grid[0])

        r = n-1
        for x in range(m):
            while grid[r][x] < 0:
                resp += m-x
                if r == 0:
                    return resp
                r -= 1

        return resp

    def countNegatives_3(self, grid: List[List[int]]) -> int:
        resp = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] < 0:
                    resp += len(grid[0]) - x
                    break

        return resp

    def countNegatives_2(self, grid: List[List[int]]) -> int:
        resp = 0

        def bs(a: List[int], v: int) -> int:
            l, r = 0, len(a)-1
            while l <= r:
                m = (r+l)//2
                if a[m] >= v:
                    l = m+1
                else:
                    r = m-1
            return l

        for row in grid:
            pos = bs(row, 0)
            resp += len(row) - pos
        return resp

    def countNegatives_1(self, grid: List[List[int]]) -> int:
        resp = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] < 0:
                    resp += 1

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.countNegatives(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[4,   3,  2, -1],
                [3,   2,  1, -1],
                [1,   1, -1, -2],
                [-1, -1, -2, -3]],
            8)
    do_test(1, [[3, 2], [1, 0]], 0)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        d = Deque()
        for y in range(len(grid)):
            d.append((0, y))
            d.append((len(grid[0])-1, y))
        for x in range(len(grid[0])):
            d.append((x, 0))
            d.append((x, len(grid)-1))

        while d:
            x, y = d.popleft()
            if grid[y][x] != 1:
                continue
            grid[y][x] = -1
            if x > 0:
                d.append((x-1, y))
            if x < len(grid[0])-1:
                d.append((x+1, y))
            if y > 0:
                d.append((x, y-1))
            if y < len(grid)-1:
                d.append((x, y+1))

        s = 0
        for line in grid:
            s += line.count(1)
        return s


def do_test(i: int, s, r):
    c = Solution()
    resp = c.numEnclaves(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 3)
    do_test(1, [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], 0)
    do_test(2, [
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    ], 3)

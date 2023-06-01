from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


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


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        if grid[-1][-1] != 0 or grid[0][0] != 0:
            return -1
        if h == 1 and w == 1:
            return 1

        q = Deque()
        q.append((0, 0, 1))
        grid[0][0] = 2

        while q:
            x, y, l = q.popleft()
            if y == h-1 and x == w-1:
                return l

            for nx, ny in get_nb(x, y, w-1, h-1, dia=True):
                if grid[ny][nx] != 0:
                    continue
                grid[ny][nx] = 2
                q.append((nx, ny, l+1))

        return -1


def do_test(i: int, s, r):
    c = Solution()
    resp = c.shortestPathBinaryMatrix(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[0, 1], [1, 0]], 2)
    do_test(1, [[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4)
    do_test(2, [[1, 0, 0],
                [1, 1, 0],
                [1, 1, 0]], -1)

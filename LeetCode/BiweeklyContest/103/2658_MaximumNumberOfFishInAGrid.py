from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        resp = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    continue
                q = []
                q.append((y, x))
                cur = 0
                while q:
                    y1, x1 = q.pop()
                    if grid[y1][x1] == 0:
                        continue
                    cur += grid[y1][x1]
                    grid[y1][x1] = 0
                    if x1 > 0:
                        q.append((y1, x1-1))
                    if x1 < len(grid[0])-1:
                        q.append((y1, x1+1))
                    if y1 > 0:
                        q.append((y1-1, x1))
                    if y1 < len(grid)-1:
                        q.append((y1+1, x1))

                resp = max(resp, cur)

        return resp

    def findMaxFish(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        resp = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 0:
                    continue
                q = []
                q.append((y, x))
                cur = 0
                while q:
                    y1, x1 = q.pop()
                    if grid[y1][x1] == 0:
                        continue
                    cur += grid[y1][x1]
                    grid[y1][x1] = 0
                    for r, l in get_nb(x1, y1, w-1, h-1):
                        q.append((l, r))

                resp = max(resp, cur)

        return resp


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False):
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

def do_test(i: int, s, r):
    c = Solution()
    resp = c.findMaxFish(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]], 7)
    do_test(1, [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 1)
    do_test(2, [[1, 0], [0, 0], [0, 0], [0, 0]], 1)

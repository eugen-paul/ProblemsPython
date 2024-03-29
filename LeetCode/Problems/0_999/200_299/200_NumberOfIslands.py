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
    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w = len(grid[0])

        resp = 0
        for r in range(h):
            for c in range(w):
                if grid[r][c] == "0":
                    continue
                resp += 1
                d = Deque()
                d.append((r, c))
                while d:
                    y, x = d.pop()
                    nbs = get_nb(x, y, w-1, h-1)
                    for nx, ny in nbs:
                        if grid[ny][nx] != "1":
                            continue
                        grid[ny][nx] = "0"
                        d.append((ny, nx))

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.numIslands(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ], 1)
    do_test(1, [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ], 3)

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
    def shortestBridge(self, grid: List[List[int]]) -> int:
        waterfront = set()
        n = len(grid)
        end = False
        # mark the first island with 2s
        for r in range(n):
            if end:
                break
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                q = Deque()
                q.append((r, c))
                grid[r][c] = 2
                while q:
                    y, x = q.popleft()
                    for nx, ny in get_nb(x, y, n-1, n-1):
                        if grid[ny][nx] == 1:
                            grid[ny][nx] = 2
                            q.append((ny, nx))
                        elif grid[ny][nx] == 0:
                            waterfront.add((ny, nx))

                end = True
                break

        # use watterwafe to get shortest way to second island
        resp = 0
        end = False
        while not end:
            next_waterfront = set()
            resp += 1

            for y, x in waterfront:
                if end:
                    break
                grid[y][x] = 2
                for nx, ny in get_nb(x, y, n-1, n-1):
                    if grid[ny][nx] == 0:
                        grid[ny][nx] = 2
                        next_waterfront.add((ny, nx))
                    elif grid[ny][nx] == 1:
                        end = True
                        break
            waterfront = next_waterfront

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.shortestBridge(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[0, 1], [1, 0]], 1)
    do_test(1, [[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2)
    do_test(2, [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], 1)
    do_test(3, [[0, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 1)

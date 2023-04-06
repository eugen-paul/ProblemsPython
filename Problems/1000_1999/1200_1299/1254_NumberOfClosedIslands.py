from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != 0:
                    continue

                d = Deque()
                d.append((x, y))
                ok = True
                while d:
                    px, py = d.popleft()
                    if grid[py][px] != 0:
                        continue

                    if px == 0 or px == len(grid[0]) - 1 or py == 0 or py == len(grid) - 1:
                        ok = False

                    grid[py][px] = -1

                    if px > 0:
                        d.append((px-1, py))
                    if px < len(grid[0])-1:
                        d.append((px+1, py))
                    if py > 0:
                        d.append((px, py-1))
                    if py < len(grid)-1:
                        d.append((px, py+1))

                if ok:
                    count += 1

        return count


def do_test(i: int, s, r):
    c = Solution()
    resp = c.closedIsland(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ], 2)
    do_test(1, [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ], 1)
    do_test(2, [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ], 2)

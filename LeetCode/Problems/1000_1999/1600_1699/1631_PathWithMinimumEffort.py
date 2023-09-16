from collections import defaultdict
from functools import cache
import heapq
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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        SEEN = set()
        q = []
        heapq.heappush(q, (0, 0, 0))
        while q:
            e, x, y = heapq.heappop(q)
            p = (x, y)
            if p in SEEN:
                continue
            SEEN.add(p)
            if p == (c-1, r-1):
                return e
            for nx, ny in get_nb(x, y, c-1, r-1):
                if (nx, ny) in SEEN:
                    continue
                heapq.heappush(q, (max(e, abs(heights[y][x] - heights[ny][nx])), nx, ny))

        return -1


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minimumEffortPath(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2)
    do_test(1, [[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1)
    do_test(2, [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]], 0)

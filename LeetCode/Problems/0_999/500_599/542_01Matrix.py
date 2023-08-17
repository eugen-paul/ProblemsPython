from collections import defaultdict
from copy import deepcopy
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
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        resp = [[-1]*n for _ in range(m)]

        q = Deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                    resp[r][c] = 0

        while q:
            y, x = q.popleft()
            nxt = get_nb(x, y, n-1, m-1)
            for nx, ny in nxt:
                if resp[ny][nx] == -1:
                    resp[ny][nx] = resp[y][x]+1
                    q.append((ny, nx))

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.updateMatrix(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    do_test(1, [[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]])


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

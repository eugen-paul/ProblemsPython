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
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        if col == 1:
            return 0

        grid = [[0]*col for _ in range(row)]

        for i, w in enumerate(cells):
            y, x = w[0]-1, w[1]-1
            nb_left = False
            nb_right = False
            color = 1
            if x == 0:
                color = 2
                nb_left = True
            if x == col-1:
                color = 3
                nb_right = True

            for nx, ny in get_nb(x, y, col-1, row-1, dia=True):
                if grid[ny][nx] == 2:
                    color = 2
                    nb_left = True
                if grid[ny][nx] == 3:
                    color = 3
                    nb_right = True

            q = Deque()
            q.append((x, y))

            while q:
                x, y = q.popleft()
                grid[y][x] = color
                if grid[ny][nx] == 2:
                    nb_left = True
                if grid[ny][nx] == 3:
                    nb_right = True
                if color != 1:
                    for nx, ny in get_nb(x, y, col-1, row-1, dia=True):
                        if grid[ny][nx] == 1:
                            grid[ny][nx] = color
                            q.append((nx, ny))
                        if grid[ny][nx] == 2:
                            nb_left = True
                        if grid[ny][nx] == 3:
                            nb_right = True

            if nb_left and nb_right:
                return i


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.latestDayToCross(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]], 2)
    do_test(1, 2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]], 1)
    do_test(2, 3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]], 3)
    do_test(3, 4, 3, [[3,1],[2,3],[1,2],[4,1],[1,1],[4,3],[3,3],[4,2],[1,3],[3,2],[2,1],[2,2]], 4)
    do_test(4, 13, 9, [[12,6],[3,4],[2,9],[9,4],[9,2],[6,4],[4,4],[8,6],[4,9],[5,6],[7,5],[12,4],[11,8],[3,7],[2,6],[9,8],[3,5],[13,4],[1,3],[10,2],[8,9],[6,6],[11,7],[11,1],[13,9],[12,7],[10,7],[8,2],[1,8],[7,3],[6,5],[2,1],[10,6],[4,8],[4,2],[9,7],[6,2],[3,6],[12,2],[10,3],[10,5],[9,5],[8,8],[8,7],[3,2],[13,6],[3,1],[5,1],[2,7],[8,3],[12,5],[11,2],[6,3],[1,4],[13,3],[4,1],[9,9],[7,7],[4,3],[12,1],[2,2],[7,6],[4,6],[7,9],[7,2],[3,8],[1,6],[11,3],[11,4],[5,9],[13,8],[1,9],[10,1],[9,1],[6,1],[10,9],[12,9],[11,5],[8,1],[13,5],[9,6],[13,2],[6,8],[2,8],[5,3],[3,3],[13,1],[11,9],[9,3],[2,4],[5,2],[8,5],[13,7],[12,8],[5,5],[7,1],[7,4],[2,5],[6,9],[4,7],[5,8],[1,5],[10,8],[8,4],[1,1],[3,9],[1,2],[7,8],[1,7],[6,7],[11,6],[4,5],[5,7],[2,3],[10,4],[5,4],[12,3]], 35)

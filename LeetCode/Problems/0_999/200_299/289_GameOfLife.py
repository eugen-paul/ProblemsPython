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
    def gameOfLife(self, board: List[List[int]]) -> None:
        h = len(board)
        b = len(board[0])

        for r in range(h):
            for c in range(b):
                nb = sum([(board[y][x]) % 10 for x, y in get_nb(c, r, b-1, h-1, dia=True)])
                if board[r][c] == 1 and (nb == 2 or nb == 3):
                    board[r][c] += 10
                elif nb == 3:
                    board[r][c] += 10

        for r in range(h):
            for c in range(b):
                board[r][c] //= 10

    def gameOfLife_1(self, board: List[List[int]]) -> None:
        h = len(board)
        b = len(board[0])

        bc = deepcopy(board)

        for r in range(h):
            for c in range(b):
                nb = sum([bc[y][x] for x, y in get_nb(c, r, b-1, h-1, dia=True)])
                if bc[r][c] == 1:
                    if nb < 2:
                        board[r][c] = 0
                    elif nb == 2 or nb == 3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 0
                else:
                    if nb == 3:
                        board[r][c] = 1


def do_test(i: int, s, r):
    c = Solution()
    c.gameOfLife(s)
    if s == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", s)


if __name__ == "__main__":
    do_test(0, [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]],
        [[0, 0, 0],
         [1, 0, 1],
         [0, 1, 1],
         [0, 1, 0]
         ]
    )
    do_test(1,
            [[1, 1],
             [1, 0]],
            [[1, 1],
             [1, 1]]
            )

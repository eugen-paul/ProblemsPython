from collections import defaultdict
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        to_check = Deque()

        for y in range(len(board)):
            if y == 0 or y == len(board)-1:
                for x in range(len(board[0])):
                    to_check.append((y, x))
            else:
                to_check.append((y, 0))
                to_check.append((y, len(board[0])-1))

        while to_check:
            y, x = to_check.pop()
            if board[y][x] != "O":
                continue

            board[y][x] = "T"

            if y > 0:
                n = board[y-1][x]
                if n == "O":
                    to_check.append((y-1, x))
            if y < len(board)-1:
                n = board[y+1][x]
                if n == "O":
                    to_check.append((y+1, x))
            if x > 0:
                n = board[y][x-1]
                if n == "O":
                    to_check.append((y, x-1))
            if x < len(board[0])-1:
                n = board[y][x+1]
                if n == "O":
                    to_check.append((y, x+1))

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "T":
                    board[y][x] = "O"
                else:
                    board[y][x] = "X"


def do_test(i: int, s, r):
    c = Solution()
    c.solve(s)
    if s == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", s)


if __name__ == "__main__":
    do_test(0, [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ], [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ])

    do_test(1, [["X"]], [["X"]])

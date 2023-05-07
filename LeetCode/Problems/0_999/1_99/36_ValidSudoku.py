from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_area(x: int, y: int, w: int, h: int) -> bool:
            b = set()
            for i in range(x, x+w):
                for j in range(y, y+h):
                    c = board[i][j]
                    if c != '.':
                        if c in b:
                            return False
                        b.add(c)
            return True

        for i in range(9):
            if not check_area(i, 0, 1, 9):
                return False

        for i in range(9):
            if not check_area(0, i, 9, 1):
                return False

        # check box
        for i in range(3):
            for j in range(3):
                if not check_area(i * 3, j * 3, 3, 3):
                    return False

        return True

    def isValidSudoku_2(self, board: List[List[str]]) -> bool:
        # check h
        for line in board:
            b = set()
            for c in line:
                if c != '.':
                    if c in b:
                        return False
                    b.add(c)

        # check_v
        for i in range(9):
            b = set()
            for j in range(9):
                c = board[j][i]
                if c != '.':
                    if c in b:
                        return False
                    b.add(c)

        # check box
        for i in range(3):
            for j in range(3):
                b = set()
                for x in range(i * 3, i * 3 + 3):
                    for y in range(j * 3, j * 3 + 3):
                        c = board[x][y]
                        if c != '.':
                            if c in b:
                                return False
                            b.add(c)
        return True


def do_test(i: int, s, r):
    c = Solution()
    resp = c.isValidSudoku(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ], True)
    do_test(1, [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ], False)
    do_test(2, [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ], False)

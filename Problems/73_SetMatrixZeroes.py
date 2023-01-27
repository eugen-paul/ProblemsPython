from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        x0 = False
        y0 = False

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == 0:
                    if x == 0:
                        x0 = True
                    if y == 0:
                        y0 = True
                    matrix[0][x] = 0
                    matrix[y][0] = 0

        for y in range(1, len(matrix)):
            for x in range(1, len(matrix[y])):
                if matrix[0][x] == 0 or matrix[y][0] == 0:
                    matrix[y][x] = 0

        if x0:
            for y in range(len(matrix)):
                matrix[y][0] = 0
        if y0:
            for x in range(len(matrix[0])):
                matrix[0][x] = 0

    def setZeroes_1(self, matrix: List[List[int]]) -> None:
        y_set = set()
        x_set = set()
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == 0:
                    y_set.add(y)
                    x_set.add(x)

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if x in x_set or y in y_set:
                    matrix[y][x] = 0


def do_test(i: int, s, r):
    c = Solution()
    resp = c.setZeroes(s)
    if s == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", s)


if __name__ == "__main__":
    do_test(0, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
    do_test(1, [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])

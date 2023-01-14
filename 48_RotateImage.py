from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        for x in range(l):
            for y in range(l):
                matrix[y][x] = (matrix[y][x] + 1000) * 2000

        for x in range(l):
            for y in range(l):
                matrix[y][x] += (matrix[l-x-1][y] // 2000)

        for x in range(len(matrix)):
            for y in range(len(matrix)):
                matrix[y][x] = (matrix[y][x] % 2000) - 1000


def do_test(i: int, s, r):
    c = Solution()
    resp = s
    c.rotate(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ])
    do_test(1, [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ],
        [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ])
    do_test(2, [
        [-1, 2, 3],
        [4, -5, 6],
        [7, 8, -9]
    ], [
        [7, 4, -1],
        [8, -5, 2],
        [-9, 6, 3]
    ])

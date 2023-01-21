from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        resp = list()

        while len(matrix) > 0:
            resp.extend(matrix.pop(0))

            if len(matrix) == 0 or len(matrix[0]) == 0:
                break
            for line in matrix:
                resp.append(line.pop())

            if len(matrix[0]) == 0:
                break
            resp.extend(reversed(matrix.pop()))

            if len(matrix) == 0:
                break
            for line in reversed(matrix):
                resp.append(line.pop(0))

        return resp

    def spiralOrder_long(self, matrix: List[List[int]]) -> List[int]:
        x_min = -1
        x_max = len(matrix[0])
        y_min = 0
        y_max = len(matrix)

        resp = list()

        x = 0
        y = 0

        while True:
            if x == x_max:
                break
            while x < x_max:
                resp.append(matrix[y][x])
                x += 1
            x_max -= 1
            x -= 1
            y += 1

            if y == y_max:
                break
            while y < y_max:
                resp.append(matrix[y][x])
                y += 1
            y_max -= 1
            x -= 1
            y -= 1

            if x == x_min:
                break
            while x > x_min:
                resp.append(matrix[y][x])
                x -= 1
            x_min += 1
            x += 1
            y -= 1

            if y == y_min:
                break
            while y > y_min:
                resp.append(matrix[y][x])
                y -= 1
            y_min += 1
            x += 1
            y += 1

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.spiralOrder(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5])
    do_test(1, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    do_test(2, [[1, 2, 3], [7, 8, 9]], [1, 2, 3, 9, 8, 7])
    do_test(3, [[1]], [1])
    do_test(4, [[1, 2], [3, 4], [5, 6], [7, 8]], [1, 2, 4, 6, 8, 7, 5, 3])

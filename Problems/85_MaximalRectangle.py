from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        max_rec = 0

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == '0':
                    matrix[y][x] = (0, 0)
                elif y == 0 and x == 0:
                    matrix[y][x] = (1, 1)
                elif y == 0:
                    matrix[y][x] = (1, matrix[y][x - 1][1] + 1)
                elif x == 0:
                    matrix[y][x] = (matrix[y-1][x][0] + 1, 1)
                else:
                    matrix[y][x] = (matrix[y - 1][x][0] + 1, matrix[y][x - 1][1]+1)

        def get_max(start_x: int, start_y: int) -> int:
            max_sub_r = matrix[start_y][start_x][0] * matrix[start_y][start_x][1]

            if max_sub_r <= max_rec:
                return max_rec

            max_sub_r = matrix[start_y][start_x][0]
            min_h = matrix[start_y][start_x][0]
            for loc_x in range(start_x-1, start_x - matrix[y][x][1], -1):
                min_h = min(min_h, matrix[start_y][loc_x][0])
                max_sub_r = max(max_sub_r, (start_x - loc_x + 1) * min_h)

            return max_sub_r

        for y in range(len(matrix)-1, -1, -1):
            for x in range(len(matrix[0])-1, -1, -1):
                max_rec = max(max_rec, get_max(x, y))

        return max_rec


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maximalRectangle(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ], 6)
    do_test(2, [
        ["1", "0", "1", "1", "1"],
        ["1", "0", "0", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "1"]
    ], 8)
    do_test(3, [
        ["1", "0", "1", "0", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ], 10)
    do_test(3, [["0"]], 0)
    do_test(4, [["1"]], 1)
    do_test(5, [["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"]], 20)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        @cache
        def ds(l: Tuple[int, int], r: Tuple[int, int]) -> bool:
            m = ((r[0]+l[0]) // 2, (r[1]+l[1]) // 2)

            if matrix[l[0]][l[1]] == target or matrix[r[0]][r[1]] == target \
                    or matrix[l[0]][r[1]] == target or matrix[r[0]][l[1]] == target:
                return True

            if l[0]+1 >= r[0] and l[1]+1 >= r[1]:
                return False

            resp = False
            if matrix[l[0]][l[1]] <= target and matrix[m[0]][m[1]] >= target:
                resp = ds(l, m)

            if matrix[m[0]][l[1]] <= target and matrix[r[0]][m[1]] >= target:
                resp = resp or ds((m[0], l[1]), (r[0], m[1]))

            if matrix[l[0]][m[1]] <= target and matrix[m[0]][r[1]] >= target:
                resp = resp or ds((l[0], m[1]), (m[0], r[1]))

            if matrix[m[0]][m[1]] <= target and matrix[r[0]][r[1]] >= target:
                resp = resp or ds(m, r)

            return resp

        return ds((0, 0), (len(matrix)-1, len(matrix[0])-1))

    def searchMatrix_i(self, matrix: List[List[int]], target: int) -> bool:
        """internet solution:
        https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/3231791/240-time-91-4-and-space-98-52-solution-with-step-by-step-explanation/
        """
        row, col = 0, len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.searchMatrix(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5, True)
    do_test(1, [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 20, False)
    do_test(2, [[1]], 1, True)
    do_test(3, [[1]], 2, False)

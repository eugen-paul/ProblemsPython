from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l <= r:
            m = l+(r-l) // 2
            if matrix[m][0] == target:
                return True
            if matrix[m][0] > target:
                r = m-1
            else:
                l = m+1

        y = r

        l = 0
        r = len(matrix[0])-1

        while l <= r:
            m = l+(r-l) // 2
            if matrix[y][m] == target:
                return True
            if matrix[y][m] > target:
                r = m-1
            else:
                l = m+1

        return False


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.searchMatrix(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True)
    do_test(1, [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False)
    do_test(2, [[1, 3]], 1, True)
    do_test(3, [[1, 3]], 3, True)
    do_test(4, [[1], [3]], 3, True)
    do_test(5, [[1], [3]], 3, True)

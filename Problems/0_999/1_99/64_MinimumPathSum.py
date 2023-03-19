from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for x in range(m):
            for y in range(n):
                left = 0
                if x > 0:
                    left = grid[y][x-1]
                up = 0
                if y > 0:
                    up = grid[y-1][x]
                if x > 0 and y > 0:
                    grid[y][x] += min(up, left)
                elif x > 0:
                    grid[y][x] += left
                elif y > 0:
                    grid[y][x] += up

        return grid[y][x]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minPathSum(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7)
    do_test(1, [[1, 2, 3], [4, 5, 6]], 12)

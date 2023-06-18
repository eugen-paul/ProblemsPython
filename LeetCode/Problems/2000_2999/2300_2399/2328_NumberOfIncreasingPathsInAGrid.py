from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)

MOD = 10**9+7


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
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        def comp(x: int, y: int) -> int:
            if dp[y][x] != -1:
                return dp[y][x]

            resp = 1

            for nx, ny in get_nb(x, y, n-1, m-1):
                if grid[ny][nx] < grid[y][x]:
                    resp = (resp + comp(nx, ny)) % MOD

            dp[y][x] = resp
            return resp

        resp = 0
        for y in range(m):
            for x in range(n):
                resp = (resp + comp(x, y)) % MOD
        return resp

    def countPaths_s(self, grid: List[List[int]]) -> int:
        """sample solution"""
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Initialize dp, 1 stands for the path made by a cell itself.
        dp = [[1] * n for _ in range(m)]

        # Sort all cells by value.
        cell_list = [[i, j] for i in range(m) for j in range(n)]
        cell_list.sort(key=lambda x: grid[x[0]][x[1]])

        # Iterate over the sorted cells, for each cell grid[i][j]:
        for i, j in cell_list:
            # Check its four neighbor cells, if a neighbor cell grid[curr_i][curr_j] has a
            # larger value, increment dp[curr_i][curr_j] by dp[i][j]
            for di, dj in directions:
                curr_i, curr_j = i + di, j + dj
                if 0 <= curr_i < m and 0 <= curr_j < n and grid[curr_i][curr_j] > grid[i][j]:
                    dp[curr_i][curr_j] += dp[i][j]
                    dp[curr_i][curr_j] %= mod

        # Sum over dp[i][j].
        return sum(sum(row) % mod for row in dp) % mod


def do_test(i: int, s, r):
    c = Solution()
    resp = c.countPaths(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 1], [3, 4]], 8)
    do_test(1, [[1], [2]], 3)
    do_test(2, [[12469, 18741, 68716, 30594, 65029, 44019, 92944, 84784, 92781, 5655, 43120, 81333, 54113, 88220, 23446, 6129, 2904, 48677, 20506, 79604, 82841, 3938, 46511, 60870, 10825, 31759, 78612, 19776, 43160,
            86915, 74498, 38366, 28228, 23687, 40729, 42613, 61154, 22726, 51028, 45603, 53586, 44657, 97573, 61067, 27187, 4619, 6135, 24668, 69634, 24564, 30255, 51939, 67573, 87012, 4106, 76312, 28737, 7704, 35798]], 148)

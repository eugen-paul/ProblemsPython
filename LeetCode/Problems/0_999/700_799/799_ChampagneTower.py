from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (query_row+1) for _ in range(query_row+1)]
        dp[0][0] = poured
        for row in range(1, query_row+1):
            for col in range(row+1):
                if col > 0 and dp[row-1][col-1] > 1.0:
                    dp[row][col] += (dp[row-1][col-1] - 1.0) / 2
                if col < row and dp[row-1][col] > 1.0:
                    dp[row][col] += (dp[row-1][col] - 1.0) / 2
        return min(1.0, dp[query_row][query_glass])


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.champagneTower(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 1, 1, 1, 0.0)
    do_test(1, 2, 1, 1, 0.5)
    do_test(2, 100000009, 33, 17, 1.0)


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

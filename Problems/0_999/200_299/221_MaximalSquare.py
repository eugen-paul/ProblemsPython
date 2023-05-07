from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        w = len(matrix[0])

        resp = 0
        dp = [[0]*(w+1) for _ in range(h+1)]
        for r in range(h):
            for c in range(w):
                if matrix[r][c] == "0":
                    continue
                dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                resp = max(resp, dp[r+1][c+1])
        return resp*resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maximalSquare(s)
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
    ], 4)
    do_test(1, [["0", "1"], ["1", "0"]], 1)
    do_test(2, [["0"]], 0)

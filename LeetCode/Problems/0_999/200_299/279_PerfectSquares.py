from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf] * (n+1)
        self.best = inf

        def solve(n: int, cur: int):
            if self.best <= cur:
                return
            if n == 0:
                self.best = cur
                return
            if dp[n] <= cur:
                return
            dp[n] = cur
            sq = int(math.sqrt(n))
            for i in range(sq, 0, -1):
                solve(n-i*i, cur+1)

        solve(n, 0)
        return self.best

    def numSquares_1(self, n: int) -> int:
        dp = [-1] * (n+1)
        dp[0] = 0

        def solve(n: int) -> int:
            if dp[n] != -1:
                return dp[n]
            sq = int(math.sqrt(n))
            resp = inf
            for i in range(1, sq+1):
                resp = min(resp, 1+solve(n-i*i))
            dp[n] = resp
            return resp

        return solve(n)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.numSquares(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 12, 3)
    do_test(1, 13, 2)
    do_test(2, 9990, 3)
    do_test(3, 8935, 4)

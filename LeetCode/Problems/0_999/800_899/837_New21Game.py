from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """sample solution"""
        dp = [0] * (n + 1)
        dp[0] = 1
        s = 1 if k > 0 else 0
        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]
        return sum(dp[k:])

    def new21Game_1(self, n: int, k: int, maxPts: int) -> float:
        """to slow"""
        dp = [0] * (k+maxPts)
        dp[0] = 1

        pr = 1 / maxPts
        for start in range(k):
            for i in range(start + 1, min(k+maxPts, start+maxPts+1)):
                dp[i] = dp[start] * pr + dp[i]

        return sum(dp[k:n+1])


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.new21Game(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 10,  1, 10, 1)
    do_test(1,  6,  1, 10, 0.6)
    do_test(2, 21, 17, 10, 0.73278)
    do_test(3, 5710, 5070, 8516, 0.13649394685476995)

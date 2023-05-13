from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)
        dp[0] = 1

        resp = 0

        for i in range(1, high+1):
            zp = max(0, i-zero)
            zm = 1 if i >= zero else 0

            op = max(0, i-one)
            om = 1 if i >= one else 0

            dp[i] = (dp[zp]*zm + dp[op]*om) % 1000000007
            if low <= i and i <= high:
                resp = (resp + dp[i]) % 1000000007

        return resp

    def countGoodStrings_1(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)
        dp[0] = 1

        for i in range(1, high+1):
            zp = max(0, i-zero)
            zm = 1 if i >= zero else 0

            op = max(0, i-one)
            om = 1 if i >= one else 0

            dp[i] = dp[zp]*zm + dp[op]*om

        return sum(dp[low:high+1]) % 1000000007


def do_test(i: int, s, j, k, l, r):
    c = Solution()
    resp = c.countGoodStrings(s, j, k, l)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 3, 1, 1, 8)
    do_test(1, 2, 3, 1, 2, 5)

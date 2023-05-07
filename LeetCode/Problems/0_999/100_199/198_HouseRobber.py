from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def rob(self, nums: List[int]) -> int:
        ll = 0
        l = 0

        for n in nums:
            cur = max(l, ll+n)
            ll, l = l, cur

        return cur

    def rob_1(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums)+2)]

        for i, n in enumerate(nums):
            dp[i+2] = max(dp[i+1], dp[i]+n)

        return dp[-1]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.rob(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 1], 4)
    do_test(1, [2, 7, 9, 3, 1], 12)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()

        def is_ok(r) -> bool:
            cnt = 0
            prev = False
            for i in range(1, len(nums)):
                if not prev and nums[i] - nums[i-1] <= r:
                    cnt += 1
                    prev = True
                else:
                    prev = False
            return cnt >= p

        l, r = 0, nums[-1]
        while l <= r:
            m = (l+r)//2
            if is_ok(m):
                r = m-1
            else:
                l = m+1
        return l

    def minimizeMax_mle(self, nums: List[int], p: int) -> int:
        """Memory Limit Exceeded :("""
        nums.sort()

        dp = [[-1] * (p+1) for _ in range(len(nums)+1)]
        for i in range(p+1):
            dp[-2][i] = inf
            dp[-1][i] = inf

        def solve(i: int, rst: int):
            if rst == 0:
                return 0
            if dp[i][rst] != -1:
                return dp[i][rst]
            dp[i][rst] = min(
                solve(i+1, rst),
                max(nums[i+1]-nums[i], solve(i+2, rst-1))
            )
            return dp[i][rst]

        return solve(0, p)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minimizeMax(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [10, 1, 2, 7, 1, 3], 2, 1)
    do_test(1, [4, 2, 1, 2], 1, 0)
    do_test(2, [0, 3], 1, 3)

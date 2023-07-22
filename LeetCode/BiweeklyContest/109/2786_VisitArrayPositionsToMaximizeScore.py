from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        m = dict()

        def solve(pos, par) -> int:
            if pos == len(nums):
                return 0
            if (pos, par) in m:
                return m[(pos, par)]
            curPar = nums[pos] & 1
            if curPar == par:
                t1 = solve(pos+1, curPar) + nums[pos]
            else:
                t1 = solve(pos+1, curPar) + nums[pos] - x
            t2 = solve(pos+1, par)
            resp = max(t1, t2)
            m[(pos, par)] = resp
            return resp

        return solve(1, nums[0] & 1) + nums[0]

    def maxScore(self, nums: List[int], x: int) -> int:
        dp = [0, 0]
        dp[nums[0] % 2] = nums[0]
        dp[1 - nums[0] % 2] = -x

        for n in nums[1:]:
            p = n % 2
            dp[p] = max(dp[p] + n, dp[1-p] + n - x)

        return max(dp)

    def maxScore_i(self, nums: List[int], x: int) -> int:
        """internet solution"""
        dp = [0, 0]
        for i in range(len(nums)-1, -1, -1):
            m = nums[i] % 2
            dp[m] = max(nums[i] + dp[m], nums[i] + dp[1-m] - x)
        return dp[nums[0] % 2]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxScore(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, 6, 1, 9, 2], 5, 13)
    do_test(1, [2, 4, 6, 8], 3, 20)
    do_test(2, [8, 50, 65, 85, 8, 73, 55, 50, 29, 95, 5, 68, 52, 79], 74, 470)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n+1)
        dp[-1] = True
        for i in range(n-1, -1, -1):
            if i <= n-2 and nums[i] == nums[i+1]:
                dp[i] = dp[i+2]
            if i <= n-3 and nums[i] == nums[i+1] and nums[i] == nums[i+2]:
                dp[i] = dp[i] or dp[i+3]
            if i <= n-3 and nums[i] == nums[i+1]-1 and nums[i] == nums[i+2]-2:
                dp[i] = dp[i] or dp[i+3]
        return dp[0]

    def validPartition_1(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def solve(pos: int) -> bool:
            if pos == n:
                return True
            check = False
            if pos <= n-2 and nums[pos] == nums[pos+1]:
                check = solve(pos+2)
            if not check and pos <= n-3 and nums[pos] == nums[pos+1] and nums[pos] == nums[pos+2]:
                check = solve(pos+3)
            if not check and pos <= n-3 and nums[pos] == nums[pos+1]-1 and nums[pos] == nums[pos+2]-2:
                check = solve(pos+3)
            return check

        return solve(0)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.validPartition(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [4, 4, 4, 5, 6], True)
    do_test(1, [1, 1, 1, 2], False)
    do_test(2, [1, 1, 1, 1, 2, 3], True)
    do_test(3, [1, 1, 2], False)

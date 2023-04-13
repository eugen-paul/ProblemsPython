from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        """very very very many help from internet"""
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]

        for block in range(len(nums)):
            for left in range(0, len(nums) - block):
                right = left + block
                for last in range(left+1, right):
                    dp[left][right] = max(dp[left][right], nums[left]*nums[last]*nums[right] + dp[left][last] + dp[last][right])

        return dp[0][-1]

    def maxCoins_i(self, nums: List[int]) -> int:
        """internet solution
        https://leetcode.com/problems/burst-balloons/solutions/3240545/312-time-90-16-solution-with-step-by-step-explanation/
        """
        # Add padding to the input array
        nums = [1] + nums + [1]
        n = len(nums)
        # Initialize a dp table to store the maximum coins for subproblems
        # dp[i][j] - the maximum coins we can get by bursting all balloons between index i and j (exclusive)
        dp = [[0] * n for _ in range(n)]

        # Iterate the input array in reverse order to fill the dp table
        for i in range(n-2, -1, -1):
            for j in range(i+2, n):
                # Iterate k from i+1 to j-1 to find the last balloon to burst
                for k in range(i+1, j):
                    # Compute the maximum coins for subproblems
                    dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])

        # The result is the maximum coins for the original problem
        return dp[0][n-1]

    def maxCoins_s(self, nums: List[int]) -> int:
        """too slow"""
        nums = [x for x in nums if x > 0]

        @cache
        def rest(re: Tuple[int]) -> int:
            if len(re) == 1:
                return re[0]

            if len(re) == 2:
                return re[0] * re[1] + max(re)

            best = 0
            for i, _ in enumerate(re):
                cur = 0
                if i == 0:
                    cur = re[0]*re[1] + rest(re[1:])
                elif i == len(re)-1:
                    cur = re[-1]*re[-2] + rest(re[:len(re)-1])
                else:
                    cur = re[i-1]*re[i]*re[i+1] + rest(re[:i] + re[i+1:])
                best = max(best, cur)
            return best

        return rest(tuple(nums))


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxCoins(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 1, 5, 8], 167)
    do_test(1, [1, 5], 10)
    do_test(2, [2, 1, 1, 1, 8], 56)
    do_test(3, [2, 1, 1, 1, 3, 9], 93)
    do_test(4, [2, 1, 2, 6, 8, 10, 3, 5, 5, 5, 7, 4, 3, 9], 3317)
    do_test(5, [2, 6, 8, 10, 7, 9], 1917)
    do_test(6, [4, 1, 4, 9, 4, 1, 8, 1, 8, 6, 9, 1, 2, 0, 9, 6, 4, 1, 7, 9, 5, 4, 4, 0], 5872)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[-1] = (1, 1)

        for start in range(len(nums)-2, -1, -1):
            max_len = 0
            max_cnt = 1
            for cur in range(start+1, len(nums)):
                if nums[start] >= nums[cur]:
                    continue
                if dp[cur][0] == max_len:
                    max_cnt += dp[cur][1]
                elif dp[cur][0] > max_len:
                    max_len = dp[cur][0]
                    max_cnt = dp[cur][1]
            dp[start] = (max_len+1, max_cnt)

        ma = 0
        resp = 0
        for l, v in dp:
            if l == ma:
                resp += v
            elif l > ma:
                resp = v
                ma = l

        return resp

    def findNumberOfLIS_s(self, nums: List[int]) -> int:
        """too slow"""
        m = defaultdict(lambda: 0)
        dp = [0] * len(nums)

        def solve(start: int, cur: int):
            for i in range(start+1, len(nums)):
                if nums[start] < nums[i]:
                    dp[start] = 1
                    solve(i, cur+1)
            m[cur] += 1

        for i in range(len(nums)):
            if dp[i] != 0:
                continue
            solve(i, 1)

        ma = max(m.keys())

        return m[ma]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findNumberOfLIS(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 5, 4, 7], 2)
    do_test(1, [2, 2, 2, 2, 2], 5)
    do_test(2, [1, 4, 2, 5], 2)
    do_test(3, [1, 2, 1, 2], 3)

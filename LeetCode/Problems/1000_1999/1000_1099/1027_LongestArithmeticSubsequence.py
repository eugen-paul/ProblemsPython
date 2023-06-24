from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [[1] * (1001) for _ in range(1001)]

        resp = 0
        for s in range(len(nums)):
            for e in range(s+1, len(nums)):
                l = nums[e]-nums[s]+500
                dp[e][l] = dp[s][l] + 1
                resp = max(resp, dp[e][l])
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestArithSeqLength(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 6, 9, 12], 4)
    do_test(1, [9, 4, 7, 2, 10], 3)
    do_test(2, [20, 1, 15, 3, 10, 5, 8], 4)

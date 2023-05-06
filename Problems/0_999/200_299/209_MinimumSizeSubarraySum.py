from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0

        s = 0
        resp = inf
        for r in range(len(nums)):
            s += nums[r]
            while s-nums[l] >= target:
                s -= nums[l]
                l += 1
            if s >= target:
                resp = min(resp, r-l+1)

        return resp if resp != inf else 0


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minSubArrayLen(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 7, [2, 3, 1, 2, 4, 3], 2)
    do_test(1, 4, [1, 4, 4], 1)
    do_test(2, 11, [1, 1, 1, 1, 1, 1, 1, 1], 0)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        resp = 0
        pre, last = -1, 0
        for n in nums:
            if n == 1:
                last += 1
            else:
                pre = last
                last = 0
            resp = max(pre+last, resp)

        return resp

    def longestSubarray(self, nums: List[int]) -> int:
        l, z, resp = 0, 0, 0

        for r, n in enumerate(nums):
            if n == 0:
                z += 1
            while z > 1:
                if nums[l] == 0:
                    z -= 1
                l += 1
            resp = max(resp, r-l)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestSubarray(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 1, 0, 1], 3)
    do_test(1, [0, 1, 1, 1, 0, 1, 1, 0, 1], 5)
    do_test(2, [1, 1, 1], 2)
    do_test(3, [0, 0, 0], 0)
    do_test(4, [1, 0, 1, 0], 2)

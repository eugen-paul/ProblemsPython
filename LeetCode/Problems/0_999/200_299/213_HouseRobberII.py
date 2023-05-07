from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def cmp(nums: List[int]) -> int:
            ll = 0
            l = 0

            for i in range(len(nums)):
                cur = max(l, ll+nums[i])
                ll = l
                l = cur
            return l

        return max(cmp(nums[1:]), cmp(nums[:len(nums)-1]))

    def rob_1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ll = 0
        l = 0

        for i in range(1, len(nums)):
            cur = max(l, ll+nums[i])
            ll = l
            l = cur
        without_1 = l

        ll = 0
        l = 0
        for i in range(len(nums)-1):
            cur = max(l, ll+nums[i])
            ll = l
            l = cur
        without_last = l

        return max(without_1, without_last)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.rob(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, 2], 3)
    do_test(1, [1, 2, 3, 1], 4)
    do_test(2, [1, 2, 3], 3)
    do_test(3, [3], 3)

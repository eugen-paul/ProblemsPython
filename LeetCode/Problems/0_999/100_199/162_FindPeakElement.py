from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # first element is greater than neighbors
        if nums[0] > nums[1]:
            return 0
        # last element is greater than neighbors
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r+l) // 2
            # current position is greater than neighbors
            if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m
            # On the line side there is a maximum.
            if nums[l] >= nums[m] or nums[m] < nums[m-1]:
                r = m
            else:
                l = m

        return l + 1

    def findPeakElement_i(self, nums: List[int]) -> int:
        """sample solution"""
        if len(nums) == 1:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            m = (r+l) // 2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m+1

        return l


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findPeakElement(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 1], 2)
    do_test(1, [1, 2, 1, 3, 5, 6, 4], 5)
    do_test(2, [4, 5, 6, 7, 8, 9, 10], 6)
    do_test(3, [4, 5, 6, 7, 8, 9, 1], 5)
    do_test(4, [4, 5, 4, 5, 4, 5], 5)
    do_test(5, [4, 5, 4, 5, 4], 1)
    do_test(6, [4, 3, 2, 1], 0)
    do_test(7, [1, 2, 3, 4, 5, 6, 7, 1, 11, 10], 6)
    do_test(8, [1, 6, 5, 4, 3, 2, 1], 1)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        resp = 10_000
        while l < r:
            m = (r + l) // 2
            if nums[l] < nums[m]:
                resp = min(resp, nums[l])
                l = m + 1
            elif nums[m] < nums[r]:
                resp = min(resp, nums[m])
                r = m - 1
            else:
                resp = min(resp, nums[r])
                r -= 1

        return min(resp, nums[l])

    def findMin_i(self, nums: List[int]) -> int:
        """internet solution"""
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[start] > nums[mid]:
                end = mid
            else:
                end -= 1

        return nums[start]

    def findMin_1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 10_000
        l, r = 0, len(nums)-1
        m = (r+l)//2
        v_l = nums[l]
        v_m = nums[m]
        v_r = nums[r]
        if v_l < v_m:
            return min(v_l, self.findMin(nums[m+1:]))
        if v_m < v_r:
            return min(v_m, self.findMin(nums[:m]))
        return min(self.findMin(nums[m+1:]), self.findMin(nums[:m]))


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findMin(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 5], 1)
    do_test(1, [2, 2, 2, 0, 1], 0)
    do_test(2, [2, 2, 3, 0, 1], 0)
    do_test(3, [2, 0, 2, 2, 2], 0)
    do_test(4, [3, 4, 5, 1, 2], 1)
    do_test(5, [4, 5, 6, 7, 0, 1, 2], 0)
    do_test(6, [11, 13, 15, 17], 11)
    do_test(7, [11], 11)
    do_test(8, [1, 2], 1)
    do_test(9, [2, 1], 1)
    do_test(10, [1, 2, 3], 1)
    do_test(11, [2, 3, 1], 1)
    do_test(12, [3, 1, 2], 1)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """with internet help"""
        k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

    def rotate_1(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        s = nums[len(nums) - k:] + nums[:len(nums) - k]
        for i, n in enumerate(s):
            nums[i] = n

    def rotate_1(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        d = Deque()
        for i in range(k):
            d.append(nums[len(nums) - i - 1])
        for i in range(len(nums) - 1, k-1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = d.pop()


def do_test(i: int, s, n, r):
    c = Solution()
    c.rotate(s, n)
    if s == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", s)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
    do_test(1, [-1, -100, 3, 99], 2, [3, 99, -1, -100])
    do_test(2, [1, 2, 3, 4, 5, 6], 1, [6, 1, 2, 3, 4, 5])

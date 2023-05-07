from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.search(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [-1, 0, 3, 5, 9, 12], 9, 4)
    do_test(1, [-1, 0, 3, 5, 9, 12], 2, -1)

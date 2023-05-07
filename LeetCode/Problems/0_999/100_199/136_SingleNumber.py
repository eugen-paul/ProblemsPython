from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        resp = 0
        for n in nums:
            resp ^= n
        return resp

    def singleNumber_1(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.singleNumber(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 2, 1], 1)
    do_test(1, [4, 1, 2, 1, 2], 4)
    do_test(2, [1], 1)
    do_test(3, [1, 2, 3, 4, 5, 1, 2, 3, 4], 5)
    do_test(4, [-1, 2, -3, 4, -5, -1, 2, -3, 4], -5)

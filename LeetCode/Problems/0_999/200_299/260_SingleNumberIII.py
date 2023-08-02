from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for c in nums:
            xor ^= abs(c)

        div = 2 ** (xor.bit_length() - 1)
        a, b = 0, 0
        for c in nums:
            if abs(c) & div:
                a ^= c
            else:
                b ^= c
        return [a, b]

    def singleNumber_1(self, nums: List[int]) -> List[int]:
        nums.sort()
        resp = []
        for i, c in enumerate(nums):
            if i == 0 and nums[i] != nums[i+1]:
                resp += [c]
            elif i == len(nums)-1 and nums[i-1] != nums[i]:
                resp += [c]
            elif nums[i-1] != nums[i] and nums[i] != nums[i+1]:
                resp += [c]
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.singleNumber(s)
    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", sorted(r), "response", sorted(resp))


if __name__ == "__main__":
    # do_test(0, [1, 2, 1, 3, 2, 5], [3, 5])
    # do_test(1, [-1, 0], [-1, 0])
    # do_test(2, [0, 1], [1, 0])
    do_test(2, [-4, 5], [-4, 5])

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = [0] * 32
        for n in nums:
            n += 2**31
            for i in range(32):
                c[i] += 1 if n & (1 << i) != 0 else 0
        resp = 0
        for i, n in enumerate(c):
            resp += (2**i) * (n % 3)
        return resp - 2**31

    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k, v in c.items():
            if v == 1:
                return k

    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-2, 3):
            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]

    def singleNumber_i(self, nums: List[int]) -> int:
        """internet solution"""
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones


def do_test(i: int, s, r):
    c = Solution()
    resp = c.singleNumber(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 2, 3, 2], 3)
    do_test(1, [0, 1, 0, 1, 0, 1, 99], 99)
    do_test(2, [0, 1, 0, 1, 0, 1, -99], -99)
    do_test(3, [0, -1, 0, -1, 0, -1, 99], 99)

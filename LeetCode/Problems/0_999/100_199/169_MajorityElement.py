from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement_1(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common(1)[0][0]

    def majorityElement_i(self, nums):
        """sample solution"""
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


def do_test(i: int, s, r):
    c = Solution()
    resp = c.majorityElement(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 2, 3], 3)
    do_test(1, [2, 2, 1, 1, 1, 2, 2], 2)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def sub(f: int, t: int) -> int:
            if t < f:
                return 0
            if t-f == 0:
                return nums[t]
            prd = 1
            first, last = None, 1
            for i in range(f, t+1):
                prd *= nums[i]
                last *= nums[i]
                if nums[i] < 0:
                    if first is None:
                        first = prd
                    last = nums[i]

            if prd > 0:
                return prd

            return max(prd // first, prd//last)

        best = nums[0]
        start = 0
        for i, n in enumerate(nums):
            if n == 0:
                best = max(best, sub(start, i-1), 0)
                start = i+1
        best = max(best, sub(start, i))

        return best

    def maxProduct_i(self, nums: List[int]) -> int:
        """internet solution"""
        curMax, curMin = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)

            res = max(res, curMax)

        return res

    def maxProduct_1(self, nums: List[int]) -> int:
        def sub(subs: List[int]) -> int:
            if len(subs) == 0:
                return 0
            if len(subs) == 1:
                return subs[0]
            prd = 1
            for n in subs:
                prd *= n

            if prd > 0:
                return prd

            first = 1
            for n in subs:
                first *= n
                if n < 0:
                    break
            last = 1
            for n in reversed(subs):
                last *= n
                if n < 0:
                    break
            return max(prd // first, prd//last)

        best = nums[0]
        s = []
        for n in nums:
            if n != 0:
                s.append(n)
            else:
                best = max(best, sub(s), 0)
                s.clear()
        best = max(best, sub(s))

        return best


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxProduct(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, -2, 4], 6)
    do_test(1, [-2, 0, -1], 0)
    do_test(2, [2, -3, -2, 4], 48)
    do_test(3, [-2, -1], 2)
    do_test(4, [-2, -1, 0], 2)
    do_test(5, [0, -2, -1, 0], 2)
    do_test(6, [0], 0)
    do_test(7, [0, 0, 0, 0, 0], 0)
    do_test(8, [0, 3, 0, 2, 0], 3)
    do_test(9, [0, 3, 0, 4, 0], 4)

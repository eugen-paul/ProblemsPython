from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """With the hint that the solution is binary search."""
        def check(target_sum) -> bool:
            parts = 1
            curr = 0
            for n in nums:
                if curr+n > target_sum:
                    curr = n
                    parts += 1
                else:
                    curr += n
            return parts <= k

        l, r = max(nums), sum(nums)

        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l

    def splitArray_1(self, nums: List[int], k: int) -> int:
        @cache
        def sub(start: int, rest: int) -> int:
            if rest == 1:
                return sum(nums[start:])

            cur = 0
            best = inf
            for i in range(start, len(nums) - rest + 1):
                cur += nums[i]
                if cur >= best:
                    break
                best = max(cur, sub(i+1, rest-1))
            return best

        return sub(0, k)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.splitArray(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [7, 2, 5, 10, 8], 2, 18)
    do_test(1, [1, 2, 3, 4, 5], 2, 9)
    do_test(2, [1, 4, 4], 3, 4)
    do_test(3, [10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8], 8, 25)

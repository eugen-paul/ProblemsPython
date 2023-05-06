import bisect
from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        resp = 0
        for i, n in enumerate(nums):
            rest = target - n
            if rest < n:
                break
            pos = bisect.bisect_right(nums, rest)
            resp += pow(2, pos-i-1, 1000000007)
            resp %= 1000000007

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.numSubseq(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 5, 6, 7], 9, 4)
    do_test(1, [3, 3, 6, 8], 10, 6)
    do_test(2, [2, 3, 3, 4, 6, 7], 12, 61)
    do_test(3, [1, 10, 1, 1], 2, 7)

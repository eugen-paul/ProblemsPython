from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s = nums[0]
        resp = s
        for i in range(1, len(nums)):
            s += nums[i]
            resp = max(resp, math.ceil(s / (i+1)))

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minimizeArrayValue(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 7, 1, 6], 5)
    do_test(1, [10, 1], 10)
    do_test(2, [13, 13, 20, 0, 8, 9, 9], 16)

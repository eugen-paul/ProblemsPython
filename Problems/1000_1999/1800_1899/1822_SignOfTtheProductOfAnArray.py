from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        z = len([x for x in nums if x == 0])
        n = len([x for x in nums if x < 0])
        if z > 0:
            return 0
        if n & 1 == 1:
            return -1
        return 1

    def arraySign_1(self, nums: List[int]) -> int:
        n = 0
        for c in nums:
            if c == 0:
                return 0
            if c < 0:
                n += 1
        if n & 1 == 1:
            return -1
        return 1


def do_test(i: int, s, r):
    c = Solution()
    resp = c.arraySign(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [-1, -2, -3, -4, 3, 2, 1], 1)
    do_test(1, [1, 5, 0, 2, -3], 0)
    do_test(2, [-1, 1, -1, 1, -1], -1)

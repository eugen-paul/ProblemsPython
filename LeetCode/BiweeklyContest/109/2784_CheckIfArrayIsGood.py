from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        if nums[-1] != len(nums)-1:
            return False

        sub = set(nums[:len(nums)-1])
        for i in range(1, len(nums)):
            if i not in sub:
                return False
        return True


def do_test(i: int, s, r):
    c = Solution()
    resp = c.isGood(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 1, 3], False)
    do_test(1, [1, 3, 3, 2], True)
    do_test(2, [1, 1], True)
    do_test(3, [3, 4, 4, 1, 2, 1], False)

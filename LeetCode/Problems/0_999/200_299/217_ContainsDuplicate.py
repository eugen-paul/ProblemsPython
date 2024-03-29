from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.containsDuplicate(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 1], True)
    do_test(1, [1, 2, 3, 4], False)
    do_test(2, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)

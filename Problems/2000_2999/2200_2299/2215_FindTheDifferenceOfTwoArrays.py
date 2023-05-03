from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        return [list(s1-s2), list(s2-s1)]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findDifference(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]])
    do_test(1, [1, 2, 3, 3], [1, 1, 2, 2], [[3], []])

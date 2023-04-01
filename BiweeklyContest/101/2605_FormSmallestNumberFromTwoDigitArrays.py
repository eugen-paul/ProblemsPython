from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set1.intersection(set2)
        if len(set3) > 0:
            return min(set3)

        return min(nums1[0] * 10 + nums2[0], nums2[0] * 10 + nums1[0])


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minNumber(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [4, 1, 3], [5, 7], 15)
    do_test(0, [3, 5, 2, 6],  [3, 1, 7], 3)

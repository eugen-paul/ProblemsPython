from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def peakIndexInMountainArray_s(self, arr: List[int]) -> int:
        """sample solution"""
        l = 0
        r = len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        arr = [-inf] + arr + [-inf]
        l, r = 0, len(arr)-1

        while True:
            m = (l+r) // 2
            if arr[m-1] < arr[m] and arr[m] > arr[m+1]:
                return m-1
            if arr[m-1] < arr[m] and arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m-1


def do_test(i: int, s, r):
    c = Solution()
    resp = c.peakIndexInMountainArray(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, [0, 1, 0], 1)
    # do_test(1, [0, 2, 1, 0], 1)
    # do_test(2, [0, 10, 5, 2], 1)
    do_test(3, [0, 10, 5, 2, 1], 1)
    do_test(4, [0, 1, 5, 20, 1], 3)

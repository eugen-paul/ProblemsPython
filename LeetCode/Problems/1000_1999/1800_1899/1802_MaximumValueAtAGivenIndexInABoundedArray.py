from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        l, r = 1, maxSum
        while l <= r:
            m = (r+l)//2

            h = m
            left = (m-1)*m // 2
            if h-1 < index:
                left += index - h + 1
            elif h-1 > index:
                left -= (h - 1 - index) * (h - 1 - index + 1) // 2

            right = (m-1)*m // 2
            if n - index - 1 > h-1:
                right += n - index - h
            elif n - index - 1 < h-1:
                a = h-1-(n-index-1)
                b = h-1-(n-index-1)+1
                right -= (a) * (b) // 2

            if h+left+right > maxSum:
                r = m-1
            else:
                l = m+1

        return l-1


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.maxValue(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, 2, 6, 2)
    do_test(1, 6, 1, 10, 3)

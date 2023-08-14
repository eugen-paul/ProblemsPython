from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.reverse()
        l, r = 0, len(citations)-1
        while l <= r:
            m = (r+l)//2
            if citations[m] >= m+1:
                l = m+1
            else:
                r = m-1
        return l

    def hIndex_1(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, len(citations)
        while l < r and r != 0:
            m = (r+l)//2+1
            if citations[n-1-(m-1)] >= m:
                l = m
            else:
                r = m-1

        return l


def do_test(i: int, s, r):
    c = Solution()
    resp = c.hIndex(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [0, 1, 3, 5, 6], 3)
    do_test(1, [1, 2, 100], 2)
    do_test(2, [1, 1, 1, 3, 3], 2)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def is_ok(h: int) -> bool:
            pos = 0
            for n in citations:
                if n >= h:
                    pos += 1
            return pos >= h

        l, r = 0, len(citations)
        while l <= r:
            m = (l+r)//2
            if is_ok(m):
                l = m+1
            else:
                r = m-1
        return l-1

    def hIndex_1(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if i+1 > citations[i]:
                return i
        return len(citations)

    def hIndex_i(self, citations: List[int]) -> int:
        """internet solution:
        https://leetcode.com/problems/h-index/solutions/3602383/explained-simple-and-clear-python3-code/
        """
        c = sorted(citations)
        n = len(c)
        for i in range(n):
            if c[i] >= n-i:
                return n-i
        return 0


def do_test(i: int, s, r):
    c = Solution()
    resp = c.hIndex(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 0, 6, 1, 5], 3)
    do_test(1, [1, 3, 1], 1)
    do_test(2, [1, 1, 1], 1)
    do_test(3, [1, 1, 1, 3, 3], 2)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def is_ok(t: int) -> bool:
            extra = 0
            for p in batteries:
                extra += min(p, t)

            return extra // n >= t

        l, r = 0, sum(batteries)
        while l < r:
            m = (r+l+1)//2
            if is_ok(m):
                l = m
            else:
                r = m-1

        return l


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxRunTime(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, [3, 3, 3], 4)
    do_test(1, 2, [1, 1, 1, 1], 2)

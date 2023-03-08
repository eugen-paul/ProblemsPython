from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def is_ok(k: int) -> bool:
            hours = 0
            for n in piles:
                hours += math.ceil(n / k)
            return hours <= h

        l = 1
        r = max(piles)

        while l <= r:
            m = (r+l) // 2
            if is_ok(m):
                r = m-1
            else:
                l = m+1

        return l


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minEatingSpeed(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 6, 7, 11], 8, 4)
    do_test(1, [30, 11, 23, 4, 20], 5, 30)
    do_test(2, [30, 11, 23, 4, 20], 6, 23)

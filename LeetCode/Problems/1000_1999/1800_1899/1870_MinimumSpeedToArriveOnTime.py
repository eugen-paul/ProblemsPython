from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        l, r = 1, 10**7

        def is_ok(s: int) -> bool:
            time = 0
            for d in dist[:-1]:
                time += math.ceil(d / s)
            time += dist[-1] / s
            return time <= hour

        while l <= r:
            m = (l+r) // 2
            if is_ok(m):
                r = m-1
            else:
                l = m+1

        return l if l <= 10**7 else -1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minSpeedOnTime(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, [1, 3, 2], 6, 1)
    # do_test(1, [1, 3, 2], 2.7, 3)
    # do_test(2, [1, 3, 2], 1.9, -1)
    do_test(3, [1, 1, 100000], 2.01, 10000000)

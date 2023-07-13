import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nmb = [0, 1]

        while len(nmb) <= n:
            check = []

            div = nmb[-1] // 2
            pos = bisect.bisect_right(nmb, div)
            check.append(nmb[pos] * 2)

            div = nmb[-1] // 3
            pos = bisect.bisect_right(nmb, div)
            check.append(nmb[pos] * 3)

            div = nmb[-1] // 5
            pos = bisect.bisect_right(nmb, div)
            check.append(nmb[pos] * 5)

            nmb.append(min(check))

        return nmb[-1]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.nthUglyNumber(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 10, 12)
    do_test(1, 1, 1)
    do_test(2, 20, 36)

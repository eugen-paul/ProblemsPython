from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

MOD = 10**9+7
# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @cache
        def comp(s: int, f: int) -> int:
            if f < 0:
                return 0

            resp = 0
            if s == finish:
                resp = 1
            cur = locations[s]
            for i, n in enumerate(locations):
                if i == s:
                    continue
                resp = (resp + comp(i, f-abs(cur-n))) % MOD

            return resp

        return comp(start, fuel)


def do_test(i: int, s, n, k, l, r):
    c = Solution()
    resp = c.countRoutes(s, n, k, l)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, 6, 8, 4], 1, 3, 5, 4)
    do_test(1, [4, 3, 1], 1, 0, 6, 5)
    do_test(2, [5, 2, 1], 0, 2, 3, 0)

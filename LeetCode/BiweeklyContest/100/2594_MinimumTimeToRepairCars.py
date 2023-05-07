from collections import defaultdict
from functools import cache
from math import inf, sqrt
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_ok(time: int) -> bool:
            rest = cars
            for r in ranks:
                c2 = time // r
                rest -= int(sqrt(c2))
            return rest <= 0

        l = 0
        r = max(ranks) * cars * cars

        while l <= r:
            m = (r+l) // 2
            if is_ok(m):
                r = m-1
            else:
                l = m+1

        return l


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.repairCars(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [4, 2, 3, 1], 10, 16)
    do_test(1, [5, 1, 8], 6, 16)
    do_test(2, [5], 1, 5)

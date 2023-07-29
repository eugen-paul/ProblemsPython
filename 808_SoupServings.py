from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 10000:
            return 1

        m = dict()

        def solve(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            if (a, b) in m:
                return m[(a, b)]

            r = 0.25 * (
                sum(
                    [solve(a-100, b),
                     solve(a-75, b-25),
                     solve(a-50, b-50),
                     solve(a-25, b-75)]
                )
            )
            m[(a, b)] = r
            return r

        return solve(n, n)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.soupServings(s)
    if round(resp, 5) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 50, 0.62500)
    do_test(1, 75, 0.65625)
    do_test(2, 100, 0.71875)
    do_test(3, 150, 0.75781)
    do_test(4, 1000, 0.97657)
    do_test(5, 10000, 1)
    do_test(6, 10**9, 1)

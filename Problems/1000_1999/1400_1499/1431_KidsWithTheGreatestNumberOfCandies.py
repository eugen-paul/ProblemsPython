from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        resp = []
        for n in candies:
            resp.append(n+extraCandies >= m)
        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.kidsWithCandies(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, 5, 1, 3], 3, [True, True, True, False, True])
    do_test(1, [4, 2, 1, 1, 2], 1, [True, False, False, False, False])
    do_test(2, [12, 1, 12], 10, [True, False, True])

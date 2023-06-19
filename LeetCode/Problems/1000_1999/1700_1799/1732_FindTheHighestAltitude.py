from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        resp, cur = 0, 0
        for n in gain:
            cur = cur + n
            resp = max(resp, cur)
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.largestAltitude(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [-5, 1, 5, 0, -7], 1)
    do_test(1, [-4, -3, -2, -1, 4, 3, 2], 0)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        m = {chr(i+ord("a")-1): i for i in range(1, 27)}
        for i in range(len(chars)):
            m[chars[i]] = vals[i]

        best = 0
        cost = 0
        l = 0
        for r in range(len(s)):
            cost += m[s[r]]
            while cost < 0:
                cost -= m[s[l]]
                l += 1
            best = max(best, cost)
        return max(0, best)


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.maximumCostSubstring(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "adaa", "d", [-1000], 2)
    do_test(1, "abc", "abc", [-1, -1, -1], 0)
    do_test(2, "kqqqqqkkkq", "kq", [-6, 6], 30)

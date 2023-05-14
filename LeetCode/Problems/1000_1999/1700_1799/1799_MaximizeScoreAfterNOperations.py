from collections import defaultdict
from functools import cache
from math import gcd, inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def comp(i: int, t: Tuple[int]) -> int:
            resp = 0

            for a in range(len(t)-1):
                for b in range(a+1, len(t)):
                    tmp = i*gcd(t[a], t[b])
                    tmp += comp(i+1, t[:a] + t[a+1:b] + t[b+1:])
                    resp = max(resp, tmp)
            return resp

        return comp(1, tuple(nums))


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxScore(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2], 1)
    do_test(1, [3, 4, 6, 8], 11)
    do_test(2, [1, 2, 3, 4, 5, 6], 14)

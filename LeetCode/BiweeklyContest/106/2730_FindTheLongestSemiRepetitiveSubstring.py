from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        last = "-"
        resp = 0
        cur = 0
        lastCur = 0
        for c in s:
            if c == last:
                resp = max(resp, cur+lastCur)
                lastCur = cur
                cur = 1
            else:
                cur += 1
            last = c
        resp = max(resp, cur+lastCur)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestSemiRepetitiveSubstring(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "52233", 4)
    do_test(1, "5494", 4)
    do_test(2, "1111111", 2)
    do_test(3, "223345678", 8)
    do_test(4, "123445678", 9)

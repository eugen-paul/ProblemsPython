from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def partitionString(self, s: str) -> int:
        buf = set()
        resp = 1
        for c in s:
            if c in buf:
                resp += 1
                buf.clear()
            buf.add(c)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.partitionString(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "abacaba", 4)
    do_test(1, "ssssss", 6)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def removeStars(self, s: str) -> str:
        h = []

        for c in s:
            if c == "*":
                h.pop()
            else:
                h.append(c)

        return "".join(h)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.removeStars(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "leet**cod*e", "lecoe")
    do_test(1, "erase*****", "")

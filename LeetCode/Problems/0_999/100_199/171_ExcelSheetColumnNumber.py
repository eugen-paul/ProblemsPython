from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        resp = 0
        for c in columnTitle:
            resp *= 26
            resp += 1 + ord(c) - ord("A")
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.titleToNumber(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "A", 1)
    do_test(1, "AB", 28)
    do_test(2, "ZY", 701)

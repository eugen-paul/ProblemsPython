from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        resp = ""
        while columnNumber > 0:
            m = (columnNumber-1) % 26
            resp = chr(m + ord('A')) + resp
            columnNumber = (columnNumber-1) // 26
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.convertToTitle(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 1, "A")
    do_test(1, 28, "AB")
    do_test(2, 701, "ZY")

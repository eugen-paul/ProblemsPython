from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def trailingZeroes(self, n: int) -> int:
        resp = n // 5
        tmp = resp
        while tmp // 5 > 0:
            tmp = tmp // 5
            resp += tmp
        return resp

    def trailingZeroes_1(self, n: int) -> int:
        s = str(math.factorial(n))
        zeros = 0
        while s[len(s) - 1 - zeros] == "0":
            zeros += 1
        return zeros


def do_test(i: int, s, r):
    c = Solution()
    resp = c.trailingZeroes(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 0)
    do_test(1, 5, 1)
    do_test(2, 0, 0)
    do_test(3, 15, 3)
    do_test(4, 20, 4)
    do_test(5, 24, 4)
    do_test(6, 25, 6)
    do_test(7, 30, 7)
    do_test(8, 40, 9)
    do_test(9, 50, 12)
    do_test(10, 250, 62)

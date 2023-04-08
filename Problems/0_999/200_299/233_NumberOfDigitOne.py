from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 9:
            return 1

        s_n = str(n)
        f = n // (10 ** (len(s_n)-1))

        resp = 0
        resp += f * self.countDigitOne((10 ** (len(s_n)-1))-1)
        if f == 1:
            resp += n % (10 ** (len(s_n)-1)) + 1
        else:
            resp += 10 ** (len(s_n)-1)
        resp += self.countDigitOne(n % (10 ** (len(s_n)-1)))

        return resp

    def countDigitOne(self, n: int) -> int:
        """sample solution"""
        resp = 0

        i = 1
        while i <= n:
            d = i*10
            resp += (n//d)*i + min(max(n % d - i + 1, 0), i)
            i *= 10

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.countDigitOne(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 13, 6)
    do_test(1, 0, 0)
    do_test(2, 10, 2)
    do_test(3, 11, 4)
    do_test(4, 20, 12)
    do_test(5, 40, 14)
    do_test(6, 100, 21)
    do_test(7, 200, 140)
    do_test(8, 1000, 301)
    do_test(9, 2000, 1600)
    do_test(10, 10000, 4001)
    do_test(11, 101, 23)

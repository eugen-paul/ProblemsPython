from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def addDigits_i(self, num: int) -> int:
        """sample solution"""
        return 1 + (num - 1) % 9 if num else 0

    def addDigits_i(self, num: int) -> int:
        """sample solution"""
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

    def addDigits(self, num: int) -> int:
        while num >= 10:
            tmp = 0
            while num >= 10:
                tmp += (num % 10)
                num //= 10
            num += tmp
        return num

    def addDigits_1(self, num: int) -> int:
        s = str(num)
        while len(s) != 1:
            tmp = 0
            for c in s:
                tmp += int(c)
            s = str(tmp)
        return int(s)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.addDigits(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 38, 2)
    do_test(1, 0, 0)

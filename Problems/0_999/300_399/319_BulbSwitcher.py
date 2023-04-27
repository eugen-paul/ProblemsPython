from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.floor(math.sqrt(n))

    def bulbSwitch_1(self, n: int) -> int:
        """too slow"""
        if n == 0:
            return 0

        resp = 0
        prims = []

        def number_of_dividers(num: int) -> int:
            r = 0
            end = math.ceil(math.sqrt(num))
            for p in prims:
                if p > end:
                    break
                if num % p == 0:
                    r += 2
            if end*end == num:
                r -= 1
            return r

        for i in range(2, n+1):
            # Here I have seen that all numbers have even number of divisors, except the numbers that are square of other numbers.
            count = number_of_dividers(i)
            if count & 1 == 1:
                resp += 1
            if count == 0:
                prims.append(i)

        return resp + 1

    def bulbSwitch_1(self, n: int) -> int:
        """too slow"""
        resp = [False] * n

        for i in range(1, n+1):
            for p in range(i, n+1, i):
                resp[p-1] = not resp[p-1]

        return resp.count(True)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.bulbSwitch(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 1)
    do_test(1, 0, 0)
    do_test(2, 1, 1)
    do_test(3, 2, 1)
    do_test(4, 4, 2)
    do_test(5, 9999, 99)
    do_test(6, 9999999, 3162)

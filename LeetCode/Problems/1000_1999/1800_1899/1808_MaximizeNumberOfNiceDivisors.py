from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)

MOD = 10**9 + 7


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        q = 3
        r = primeFactors % q
        if r == 0:
            return pow(q, primeFactors // q, MOD)
        elif r == 1 and primeFactors > 3:
            return (pow(q, primeFactors // q - 1, MOD) * r * 4) % MOD
        else:
            return (pow(q, primeFactors // q, MOD) * r) % MOD


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxNiceDivisors(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 5, 6)
    do_test(1, 8, 18)
    do_test(2, 33, 177147)
    do_test(3, 50, 86093442)
    do_test(4, 70, 524237561)
    do_test(5, 73, 572712676)
    do_test(6, 1, 1)
    do_test(7, 2, 2)
    do_test(8, 3, 3)

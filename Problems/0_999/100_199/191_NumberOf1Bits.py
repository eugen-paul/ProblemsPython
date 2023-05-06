from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    def hammingWeight_2(self, n: int) -> int:
        s = f"{n:b}"
        return s.count("1")

    def hammingWeight_1(self, n: int) -> int:
        resp = 0
        while n != 0:
            if n & 1 == 1:
                resp += 1
            n = n//2
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.hammingWeight(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 1, 1)
    do_test(1, 2, 1)
    do_test(2, 3, 2)

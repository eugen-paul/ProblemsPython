from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def isHappy(self, n: int) -> bool:
        SEEN = set()

        while n != 1:
            if n in SEEN:
                return False
            SEEN.add(n)
            tmp = 0
            while n:
                rest = n % 10
                tmp += rest*rest
                n = n//10
            n = tmp
        return True


def do_test(i: int, s, r):
    c = Solution()
    resp = c.isHappy(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 19, True)
    do_test(1, 2, False)

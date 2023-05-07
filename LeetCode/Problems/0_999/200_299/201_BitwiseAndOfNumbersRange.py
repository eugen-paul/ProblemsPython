from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l = f"{left:032b}"
        r = f"{right:032b}"

        resp = 0

        for i in range(32):
            if l[i] != r[i]:
                break
            if l[i] == "1":
                resp += 2**(32-i-1)

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.rangeBitwiseAnd(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 5, 7, 4)
    do_test(1, 0, 0, 0)
    do_test(2, 1, 2147483647, 0)
    do_test(3, 1, 1, 1)
    do_test(4, 10, 10, 10)

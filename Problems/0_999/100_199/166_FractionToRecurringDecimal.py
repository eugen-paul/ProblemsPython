from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        g = int(numerator / denominator)
        r = abs(numerator) % abs(denominator)

        if r == 0:
            return str(g)

        if (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0) or (g < 0):
            resp = str(g) + "."
        else:
            resp = "-" + str(g) + "."

        denominator = abs(denominator)

        m: Dict[int, int] = dict()

        while r != 0:
            if r in m:
                f = m[r]
                return resp[:f] + "(" + resp[f:] + ")"
            m[r] = len(resp)
            r *= 10
            g = r // denominator
            r = r % denominator
            resp += str(g)

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.fractionToDecimal(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 1, 2, "0.5")
    do_test(1, 2, 1, "2")
    do_test(2, 4, 333, "0.(012)")
    do_test(3, 1, 3, "0.(3)")
    do_test(4, -50, 8, "-6.25")
    do_test(5, 7, -12, "-0.58(3)")
    do_test(6, -8, -1, "8")

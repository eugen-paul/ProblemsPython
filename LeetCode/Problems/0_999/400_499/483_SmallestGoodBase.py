from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def smallestGoodBase(self, n: str) -> str:

        def bs(base: int, base_len: int, ma: int) -> int:
            r = 1
            for _ in range(base_len - 1):
                r = r*base + 1
                if r > ma:
                    return 1
            if r < ma:
                return -1
            return 0

        def isOk(num: int, base_len: int):
            l, r = 2, num-1
            while l <= r:
                m = (r+l)//2
                re = bs(m, base_len, num)
                if re >= 0:
                    r = m-1
                else:
                    l = m+1
            return (bs(l, base_len, num) == 0, l)

        z = int(n)
        ma = bin(z)[2:]

        resp = z-1

        # Check if it is possible to get the number 11..11 of length i.
        for i in range(2, len(ma)+1):
            ok, b = isOk(z, i)
            if ok:
                resp = min(resp, b)

        return str(resp)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.smallestGoodBase(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "13", "3")
    do_test(1, "4681", "8")
    do_test(2, "1000000000000000000", "999999999999999999")

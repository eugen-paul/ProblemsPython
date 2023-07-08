from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        self.resp = inf
        self.part = 0

        f = set()
        for i in range(20):
            f.add(5**i)

        def solve(sub: str):
            if len(sub) == 0:
                self.resp = min(self.resp, self.part)
                return
            if sub[0] == "0":
                return
            if self.part >= self.resp:
                return

            num = 0
            for i, n in enumerate(sub):
                num = num*2 + int(n)
                if num not in f:
                    continue
                self.part += 1
                solve(sub[i+1:])
                self.part -= 1

        solve(s)

        return -1 if self.resp == inf else self.resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minimumBeautifulSubstrings(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "1011", 2)
    do_test(1, "111", 3)
    do_test(2, "0", -1)
    do_test(3, "10110111111011", 4)

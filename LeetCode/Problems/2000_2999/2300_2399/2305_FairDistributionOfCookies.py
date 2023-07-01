from collections import defaultdict
from functools import cache
import itertools
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k >= len(cookies):
            return max(cookies)

        self.resp = sum(cookies)

        def dp(m: List[int], rest: List[int]):
            if len(rest) == 0:
                self.resp = min(self.resp, max(m))
                return

            for i in range(len(m)):
                m[i] += rest[0]
                dp(m, rest[1:])
                m[i] -= rest[0]

        perm = itertools.combinations(cookies, k)

        for p in perm:
            rest = cookies.copy()
            for c in p:
                rest.remove(c)
            dp(list(p), rest)

        return self.resp


class Solution_1:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        m = [0] * k
        self.resp = sum(cookies)

        def dp(bag: int):
            if m.count(0) > len(cookies) - bag:
                return

            if bag == len(cookies):
                self.resp = min(self.resp, max(m))
                return

            for i in range(k):
                m[i] += cookies[bag]
                dp(bag+1)
                m[i] -= cookies[bag]

        dp(0)
        return self.resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.distributeCookies(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [8, 15, 10, 20, 8], 2, 31)
    do_test(1, [6, 1, 3, 2, 2, 4, 1, 2], 3, 7)
    do_test(2, [75027, 58436, 95472, 89426, 10786, 32325, 99823, 33237], 5, 107352)
    do_test(3, [1, 2, 3, 4, 5, 6, 7, 8], 8, 8)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        pr = []
        MOD = 10**9 + 7
        for i in range(1, n+1):
            tmp = i**x
            if tmp > n:
                break
            pr.append(tmp)

        m = dict()

        def solve(pos, rest) -> int:
            if rest == 0:
                return 1
            if pos == len(pr) or rest < 0 or rest < pr[pos]:
                return 0
            if (pos, rest) in m:
                return m[(pos, rest)]

            t1 = solve(pos+1, rest - pr[pos])
            t2 = solve(pos+1, rest)

            ans = (t1+t2) % MOD

            m[(pos, rest)] = ans
            return ans

        a = solve(0, n)
        return a


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.numberOfWays(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 10, 2, 1)
    do_test(1, 4, 1, 2)
    do_test(2, 300, 1, 872471266)
    do_test(3, 300, 2, 25)
    do_test(4, 300, 3, 0)

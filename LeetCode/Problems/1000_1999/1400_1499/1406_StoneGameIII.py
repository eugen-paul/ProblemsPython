from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        r = stoneValue[:] + [0]
        for i in range(len(stoneValue)-1, -1, -1):
            r[i] += r[i+1]

        mem = [inf for _ in range(len(stoneValue)+1)]

        def do(pos: int) -> int:
            if len(stoneValue) <= pos:
                return 0
            if mem[pos] != inf:
                return mem[pos]

            resp = -inf
            tmp_a = 0
            for am in range(1, min(4, len(stoneValue)-pos+1)):
                end_a = min(pos + am, len(stoneValue))
                tmp_a += stoneValue[end_a-1]
                enemy_rest = do(end_a)
                resp = max(tmp_a + r[end_a] - enemy_rest, resp)
            mem[pos] = resp
            return resp

        a = do(0)
        b = r[0] - a
        if a == b:
            return "Tie"
        if a > b:
            return "Alice"
        if b > a:
            return "Bob"

    def stoneGameIII_s(self, stoneValue: List[int]) -> str:
        """sample solution"""
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = stoneValue[i] - dp[i + 1]
            if i + 2 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] - dp[i + 2])
            if i + 3 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3])
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"

    def stoneGameIII_s2(self, stoneValue: List[int]) -> str:
        """sample solution"""
        n = len(stoneValue)
        not_computed = 10**9
        dp = [not_computed] * (n + 1)

        def f(i):
            if i == n:
                return 0
            if dp[i] != not_computed:
                return dp[i]
            dp[i] = stoneValue[i] - f(i + 1)
            if i + 2 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] - f(i + 2))
            if i + 3 <= n:
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - f(i + 3))
            return dp[i]

        dif = f(0)
        if dif > 0:
            return "Alice"
        if dif < 0:
            return "Bob"
        return "Tie"


def do_test(i: int, s, r):
    c = Solution()
    resp = c.stoneGameIII(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 7], "Bob")
    do_test(1, [1, 2, 3, -9], "Alice")
    do_test(2, [1, 2, 3, 6], "Tie")
    do_test(3, [-1, -2, -3], "Tie")

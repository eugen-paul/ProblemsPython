from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

        for i in range(len(s1)-1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])

        for i in range(len(s2)-1, -1, -1):
            dp[len(s1)][i] = dp[len(s1)][i+1] + ord(s2[i])

        for i in range(len(s1)-1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i+1][j],
                        ord(s2[j]) + dp[i][j+1]
                    )

        return dp[0][0]

    def minimumDeleteSum_1(self, s1: str, s2: str) -> int:
        """ok, but it need too much memory"""
        @cache
        def solve(p1: int, p2: int) -> int:
            if len(s1) == p1 or len(s2) == p2:
                return sum([ord(c) for c in s1[p1:]]) + sum([ord(c) for c in s2[p2:]])

            if s1[p1] == s2[p2]:
                return solve(p1+1, p2+1)
            return min(
                ord(s1[p1]) + solve(p1+1, p2),
                ord(s2[p2]) + solve(p1, p2+1)
            )

        return solve(0, 0)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minimumDeleteSum(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "sea", "eat", 231)
    do_test(1, "delete", "leet", 403)

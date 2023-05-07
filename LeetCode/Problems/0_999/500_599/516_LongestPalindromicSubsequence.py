from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[1] * len(s) for _ in range(len(s))]

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                dp[i-1][i] = 2

        for length in range(3, len(s) + 1):
            for start in range(len(s) - length + 1):
                end = start + length - 1

                if s[start] == s[end]:
                    dp[start][end] = dp[start+1][end-1] + 2
                else:
                    dp[start][end] = max(dp[start][end-1], dp[start+1][end])

        return dp[0][-1]

    def longestPalindromeSubseq_i(self, s: str) -> int:
        """sample solution"""
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestPalindromeSubseq(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "bbbab", 4)
    do_test(1, "cbbd", 2)
    do_test(2, "acba", 3)
    do_test(3, "acbaa", 3)
    do_test(4, "acbba", 4)
    do_test(5, "acbbaa", 4)
    do_test(6, "aca", 3)

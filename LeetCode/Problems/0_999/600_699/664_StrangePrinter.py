from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join([c for i, c in enumerate(s) if i == 0 or s[i-1] != c])

        @cache
        def solve(sub: str) -> int:
            if len(sub) == 0:
                return 0
            if len(sub) == len(set(sub)):
                return len(sub)

            resp = 1 + solve(sub[1:])

            for i in range(1, len(sub)):
                if sub[0] == sub[i]:
                    resp = min(
                        resp,
                        solve(sub[:i]) + solve(sub[i+1:])
                    )

            return resp

        return solve(s)

    def strangePrinter_s(self, s: str) -> int:
        """sample solution"""
        s = [c for i, c in enumerate(s) if i == 0 or s[i-1] != c]

        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                j = -1
                for i in range(left, right):
                    if s[i] != s[right] and j == -1:
                        j = i
                    if j != -1:
                        dp[left][right] = min(dp[left][right], 1 + dp[j][i] + dp[i + 1][right])

                if j == -1:
                    dp[left][right] = 0

        return dp[0][n - 1] + 1

    def strangePrinter_i(self, s: str) -> int:
        """internet solution:
        https://leetcode.com/problems/strange-printer/solutions/3835843/100-printer-video-peculiar-minimizing-prints-with-dynamic-programming/
        """
        n = len(s)
        dp = [[1]*n for _ in range(n)]

        for start in range(n-1, -1, -1):
            for end in range(start+1, n):
                dp[start][end] = dp[start][end-1] + 1
                for m in range(start, end):
                    if s[m] == s[end]:
                        dp[start][end] = min(
                            dp[start][end],
                            dp[start][m] + (dp[m+1][end-1] if m+1 <= end-1 else 0)
                            # (dp[start][m-1] if m-1 >= start else 0) + dp[m][end-1] #same as prev line
                        )

        return dp[0][n-1]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.strangePrinter(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "aaabbb", 2)
    do_test(1, "aba", 2)
    do_test(2, "qwertzuioplkjhgfdsayxcvbnmqwertzuioplkjhgfdsayxcvbnmqwertzuioplkjhgfdsayxcvbnmqwertzuioplkjhgfdsayxc", 97)
    do_test(3, "dddccbdbababaddcbcaabdbdddcccddbbaabddb", 15)
    do_test(4, "tbgtgb", 4)
    do_test(5, "abdaacbadbdcbdbdaadbcadadccdaaadcb", 17)
    do_test(6, "bdabcbadcddcacadacbbaddbbbacdbacadabcbdbdcd", 21)

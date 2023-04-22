from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minInsertions(self, s: str) -> int:
        """with internet help and my solution of 516. Longest Palindromic Subsequence"""
        def longestPalindromeSubseq(s: str) -> int:
            dp = [[1] * len(s) for _ in range(len(s))]

            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    dp[i-1][i] = 2

            for gap in range(3, len(s) + 1):
                for start in range(len(s) - gap + 1):
                    end = start + gap - 1

                    if s[start] == s[end]:
                        dp[start][end] = dp[start+1][end-1] + 2
                    else:
                        dp[start][end] = max(dp[start][end-1], dp[start+1][end])

            return dp[0][-1]
        
        return len(s) - longestPalindromeSubseq(s)
    
    def minInsertions_3(self, s: str) -> int:
        mem = [[-1 for _ in range(len(s))] for _ in range(len(s))]

        def comp(l: int, r: int) -> int:
            if r - l <= 0:
                return 0
            if mem[l][r] == -1:
                if s[l] == s[r]:
                    mem[l][r] = comp(l+1, r-1)
                else:
                    mem[l][r] = min(
                        comp(l, r-1) + 1,
                        comp(l+1, r) + 1
                    )
            return mem[l][r]
        return comp(0, len(s)-1)

    def minInsertions_2(self, s: str) -> int:
        @cache
        def comp(l: int, r: int) -> int:
            if r - l <= 0:
                return 0
            if s[l] == s[r]:
                return comp(l+1, r-1)
            return min(
                comp(l, r-1) + 1,
                comp(l+1, r) + 1
            )
        return comp(0, len(s)-1)

    def minInsertions_1(self, s: str) -> int:

        @cache
        def comp(sub: str) -> int:
            if len(sub) <= 1:
                return 0
            if sub[0] == sub[-1]:
                return comp(sub[1:len(sub)-1])
            return min(
                comp(sub[1:]) + 1,
                comp(sub[:-1]) + 1
            )

        return comp(s)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minInsertions(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "zzazz", 0)
    do_test(1, "mbadm", 2)
    do_test(2, "leetcode", 5)
    do_test(3, "l", 0)
    do_test(4, "la", 1)
    do_test(5, "ll", 0)

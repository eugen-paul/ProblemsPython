from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """simple, faster and working"""
        if len(s) <= 1:
            return s

        if s == s[::-1]:
            return s

        for i in range(1, len(s)):
            tmp = s[:len(s)-i]
            if tmp == tmp[::-1]:
                return s[-1:-i-1:-1] + s
        return s

    def shortestPalindrome_i(self, s: str) -> str:
        """sample solution"""
        n: int = len(s)
        rev = s[::-1]
        s_new = s + "#" + rev
        n_new = len(s_new)

        f = [0] * n_new
        for i in range(1, n_new):
            t = f[i - 1]
            while t > 0 and s_new[i] != s_new[t]:
                t = f[t - 1]
            if s_new[i] == s_new[t]:
                t += 1
            f[i] = t
        return rev[:n - f[n_new - 1]] + s

    def shortestPalindrome_1(self, s: str) -> str:
        """simple, slow but working"""
        if len(s) <= 1:
            return s

        if s == s[::-1]:
            return s

        for i in range(1, len(s)):
            tmp = s[-1:-i-1:-1] + s
            if tmp == tmp[::-1]:
                return tmp
        return s


def do_test(i: int, s, r):
    c = Solution()
    resp = c.shortestPalindrome(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "aacecaaa", "aaacecaaa")
    do_test(1, "abcd", "dcbabcd")
    do_test(2, "", "")
    do_test(3, "a", "a")
    do_test(4, "aabba", "abbaabba")
    do_test(5, "abccba", "abccba")
    do_test(6, "abbabaab", "baababbabaab")

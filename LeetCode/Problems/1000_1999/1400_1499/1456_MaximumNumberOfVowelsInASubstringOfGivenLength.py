from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = "aeiou"
        resp = 0
        cnt = 0
        l = 0

        for i, c in enumerate(s):
            if l == k:
                if s[i-l] in v:
                    cnt -= 1
            else:
                l += 1
            if c in v:
                cnt += 1
            resp = max(cnt, resp)

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxVowels(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "abciiidef", 3, 3)
    do_test(1, "aeiou", 2, 2)
    do_test(2, "leetcode", 3, 2)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = defaultdict(lambda: 0)
        for n in arr:
            m[n] = max(m[n], m[n-difference] + 1)
        return max(m.values())


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.longestSubsequence(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4], 1, 4)
    do_test(1, [1, 3, 5, 7], 1, 1)
    do_test(2, [1, 5, 7, 8, 5, 3, 4, 2, 1], -2, 4)

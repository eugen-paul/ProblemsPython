from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        score = []
        m = 0
        s = 0
        for n in nums:
            m = max(m, n)
            c = n + m
            s += c
            score.append(s)
        return score


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findPrefixScore(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, 7, 5, 10], [4, 10, 24, 36, 56])
    do_test(1, [1, 1, 2, 4, 8, 16], [2, 4, 8, 16, 32, 64])

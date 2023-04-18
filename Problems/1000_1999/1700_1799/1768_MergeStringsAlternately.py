from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        resp = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                resp += word1[i]
            if i < len(word2):
                resp += word2[i]
        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.mergeAlternately(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "abc", "pqr", "apbqcr")
    do_test(1, "ab", "pqrs", "apbqrs")
    do_test(2, "abcd", "pq", "apbqcd")

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or len(s) == 1:
            return False

        diff = 0
        s1, s2, g1, g2 = None, None, None, None
        for a, b in zip(s, goal):
            if a != b:
                diff += 1
                if diff == 1:
                    s1 = a
                    g1 = b
                elif diff == 2:
                    s2 = a
                    g2 = b
                else:
                    return False

        if diff == 1:
            return False

        if diff == 2:
            return s1 == g2 and s2 == g1

        bf = set()
        for c in s:
            if c in bf:
                return True
            bf.add(c)

        return False


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.buddyStrings(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "ab", "ba", True)
    do_test(1, "ab", "ab", False)
    do_test(2, "aa", "aa", True)
    do_test(3, "a", "a", False)
    do_test(4, "abcdefg", "abcdefg", False)
    do_test(5, "abcdegf", "abcdefg", True)
    do_test(6, "aaaaaaa", "aaaaaaa", True)
    do_test(7, "abaaaaa", "acaaaaa", False)
    do_test(8, "ccaaaaa", "acaaaaa", False)
    do_test(9, "ccaaaaa", "abaaaaa", False)

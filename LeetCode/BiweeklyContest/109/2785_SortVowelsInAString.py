from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def sortVowels(self, s: str) -> str:

        toSort = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v = [i for i in s if i in toSort]
        v.sort()

        p1 = 0
        resp = []
        for c in s:
            if c not in toSort:
                resp.append(c)
            else:
                resp.append(v[p1])
                p1 += 1

        return "".join(c for c in resp)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.sortVowels(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "lEetcOde", "lEOtcede")
    do_test(1, "lYmpH", "lYmpH")

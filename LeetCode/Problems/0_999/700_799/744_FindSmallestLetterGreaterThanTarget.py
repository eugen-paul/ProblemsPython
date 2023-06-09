from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        resp = "-"

        for c in letters:
            if target < c:
                if resp != "-" and resp > c:
                    resp = c
                elif resp == "-":
                    resp = c

        if resp == "-":
            return letters[0]
        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.nextGreatestLetter(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["c", "f", "j"], "a", "c")
    do_test(1, ["c", "f", "j"], "c", "f")
    do_test(2, ["x", "x", "y", "y", "y"], "z", "x")

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        @cache
        def solve(pos: int) -> int:
            if n == pos:
                return 0

            sub = s[pos:]
            best = inf
            for d in dictionary:
                if sub.startswith(d):
                    best = min(best, solve(pos+len(d)))
            best = min(best, 1 + solve(pos+1))
            return best

        return solve(0)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minExtraChar(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "leetscode", ["leet", "code", "leetcode"], 1)
    do_test(1, "sayhelloworld", ["hello", "world"], 3)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

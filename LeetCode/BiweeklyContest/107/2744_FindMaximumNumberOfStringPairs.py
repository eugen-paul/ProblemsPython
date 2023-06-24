from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        m = defaultdict(lambda: 0)
        for s in words:
            a, b = s[0], s[1]
            if a > b:
                a, b = b, a
            m[(a, b)] += 1
        resp = [i for i in m.values() if i == 2]
        return len(resp)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maximumNumberOfStringPairs(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["cd", "ac", "dc", "ca", "zz"], 2)
    do_test(0, ["ab", "ba", "cc"], 1)
    do_test(0, ["aa", "ab"], 0)


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

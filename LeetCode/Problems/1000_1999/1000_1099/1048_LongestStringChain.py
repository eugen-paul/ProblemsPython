from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        m: Dict[int: List[str]] = defaultdict(list)
        for w in words:
            m[len(w)].append(w)

        def is_predecessor(a: str, b: str) -> bool:
            p = 0
            e = False
            for c in a:
                if b[p] != c:
                    if e:
                        return False
                    e = True
                    p += 1
                    if b[p] != c:
                        return False
                p += 1
            return True

        @cache
        def solve(w: str) -> int:
            l = m[len(w)+1]
            r = 1
            for ww in l:
                if is_predecessor(w, ww):
                    r = max(r, solve(ww) + 1)
            return r

        ans = 0
        for w in words:
            ans = max(ans, solve(w))

        return ans


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestStrChain(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["a", "b", "ba", "bca", "bda", "bdca"], 4)
    do_test(1, ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5)
    do_test(2, ["abcd", "dbqca"], 1)


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

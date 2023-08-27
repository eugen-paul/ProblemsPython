from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        s = set(stones)
        m = {v: set() for v in stones}
        q = Deque()
        q.append((1, 1))
        while q:
            value, k = q.popleft()
            if value == stones[-1]:
                return True

            if k > 1 and value+k-1 in s and k-1 not in m[value+k-1]:
                m[value+k-1].add(k-1)
                q.append((value+k-1, k-1))
            if value+k in s and k not in m[value+k]:
                m[value+k].add(k)
                q.append((value+k, k))
            if value+k+1 in s and k+1 not in m[value+k+1]:
                m[value+k+1].add(k+1)
                q.append((value+k+1, k+1))
        return False

    def canCross_1(self, stones: List[int]) -> bool:
        s = set(stones)
        if stones[1] != 1:
            return False

        @cache
        def solve(k: int, value: int) -> bool:
            if value == stones[-1]:
                return True
            ok = False

            if k > 1 and value+k-1 in s:
                ok = solve(k-1, value+k-1)
            if not ok and value+k in s:
                ok = solve(k, value+k)
            if not ok and value+k+1 in s:
                ok = solve(k+1, value+k+1)
            return ok

        return solve(1, 1)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.canCross(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [0, 1, 3, 5, 6, 8, 12, 17], True)
    do_test(1, [0, 1, 2, 3, 4, 8, 9, 11], False)
    do_test(2, [0, 1], True)
    do_test(3, [0, 2], False)


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

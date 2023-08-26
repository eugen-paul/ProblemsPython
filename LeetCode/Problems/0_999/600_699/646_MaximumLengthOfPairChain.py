import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()

        @cache
        def solve(p: int) -> int:
            if p == n:
                return 0
            best = solve(p+1)

            for i in range(p+1, n):
                if pairs[p][1] < pairs[i][0]:
                    best = max(best, solve(i) + 1)
            return best

        return solve(0)+1

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        q = Deque([inf])
        for i in range(n-1, -1, -1):
            f, t = pairs[i]
            if q[0] > t:
                q.appendleft(f)
        return len(q)-1


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findLongestChain(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, [[1, 2], [2, 3], [3, 4]], 2)
    # do_test(1, [[1, 2], [7, 8], [4, 5]], 3)
    # do_test(2, [[1, 2], [1, 3]], 1)
    # do_test(3, [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]], 4)
    # do_test(4, [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]], 3)
    do_test(5, [[9, 10], [9, 10], [4, 5], [-9, -3], [-9, 1], [0, 3], [6, 10], [-5, -4], [-7, -6]], 5)


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

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m: Dict[Tuple, int] = defaultdict(lambda: 0)
        for r in grid:
            m[tuple(r)] += 1

        resp = 0
        for i in range(len(grid)):
            col = []
            for r in grid:
                col.append(r[i])
            resp += m[tuple(col)]

        return resp

    def equalPairs_1(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def eq(r, c) -> bool:
            for i in range(n):
                if grid[r][i] != grid[i][c]:
                    return False
            return True

        resp = 0
        for r in range(n):
            for c in range(n):
                if eq(r, c):
                    resp += 1
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.equalPairs(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1)
    do_test(1, [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3)

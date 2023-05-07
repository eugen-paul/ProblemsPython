from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        resp = []
        for row in range(len(grid[0])):
            m = 0
            for n in range(len(grid)):
                m = max(m, len(str(grid[n][row])))
            resp.append(m)
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findColumnWidth(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1], [22], [333]], [3])
    do_test(1, [[-15, 1, 3], [15, 7, 12], [5, 6, -2]], [3, 1, 2])
    do_test(2, [[0]], [1])

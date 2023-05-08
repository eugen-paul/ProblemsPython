from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        h = len(mat)
        w = len(mat[0])

        resp = 0

        for r in range(h):
            for c in range(w):
                if r == c or c == w-r-1:
                    resp += mat[r][c]

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.diagonalSum(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]], 25)
    do_test(1, [[5]], 5)

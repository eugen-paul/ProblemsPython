from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        d = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]

        m: Dict[Tuple[int, int], float] = defaultdict(float)

        m[(row, column)] = 1.0

        while k > 0:
            nxt: Dict[Tuple[int, int], float] = defaultdict(float)

            for pos, pr in m.items():
                for dx, dy in d:
                    x, y = pos[0]+dx, pos[1]+dy
                    if 0 <= x and x <= n-1 and 0 <= y and y <= n-1:
                        nxt[(x, y)] += pr / 8

            m = nxt
            k -= 1

        return sum(m.values())


def do_test(i: int, s, n, k, l, r):
    c = Solution()
    resp = c.knightProbability(s, n, k, l)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 2, 0, 0, 0.06250)
    do_test(1, 1, 0, 0, 0, 1.0)

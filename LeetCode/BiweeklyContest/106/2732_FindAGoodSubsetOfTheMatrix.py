from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m: Dict[int, int] = dict()
        for i, r in enumerate(grid):
            nm = 0
            for c in r:
                nm *= 2
                nm += c
            if nm not in m:
                m[nm] = i

        if 0 in m:
            return [m[0]]

        for a in m.keys():
            for b in m.keys():
                if a & b == 0:
                    return sorted([m[a], m[b]])

        return []


def do_test(i: int, s, r):
    c = Solution()
    resp = c.goodSubsetofBinaryMatrix(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0,  [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 1]
    ], [0, 1])

    do_test(1,  [[0]], [0])

    do_test(2,  [
        [1, 1, 1],
        [1, 1, 1]
    ], [])

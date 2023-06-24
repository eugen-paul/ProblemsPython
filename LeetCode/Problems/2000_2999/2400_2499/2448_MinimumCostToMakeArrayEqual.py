from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nc = [(n, c) for n, c in zip(nums, cost)]
        nc.sort()

        last = -1
        tmp = []
        for a, b in nc:
            if a != last:
                tmp.append((a, b))
            else:
                tmp[-1] = (a, tmp[-1][1] + b)
            last = a
        nc = tmp

        rToL = 0
        totalR = 0
        for i in range(len(nc)-1, -1, -1):
            rToL += (nc[i][0] - nc[0][0]) * nc[i][1]
            totalR += nc[i][1]

        lToR = 0
        totalL = 0
        resp = rToL
        totalR -= nc[0][1]
        for i in range(1, len(nc)):
            rToL -= totalR * (nc[i][0] - nc[i-1][0])
            totalR -= nc[i][1]
            lToR += totalL * (nc[i][0] - nc[i-1][0]) + (nc[i][0] - nc[i-1][0]) * nc[i-1][1]
            totalL += nc[i-1][1]

            resp = min(resp, lToR + rToL)

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minCost(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 5, 2], [2, 3, 1, 14], 8)
    do_test(1, [2, 2, 2, 2, 2], [4, 2, 8, 1, 3], 0)

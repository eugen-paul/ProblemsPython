from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        afterMove = []
        MOD = 10**9+7

        for n, r in zip(nums, s):
            if r == "R":
                afterMove.append(n+d)
            else:
                afterMove.append(n-d)

        afterMove.sort()

        resp = 0
        frst = afterMove[0]
        for i in range(1, len(afterMove)):
            resp = (resp + abs(afterMove[i] - frst)) % MOD

        delta = resp
        for i in range(1, len(afterMove)):
            a = abs(afterMove[i] - afterMove[i-1])
            b = len(afterMove) - i
            delta = (delta - (a * b)) % MOD
            resp = (resp + delta) % MOD

        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.sumDistance(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [-2, 0, 2], "RLL", 3, 8)
    do_test(1, [1, 0], "RL", 2, 5)

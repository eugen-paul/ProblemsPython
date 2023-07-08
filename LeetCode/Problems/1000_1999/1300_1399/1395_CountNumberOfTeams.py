from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """internet solution"""
        res = 0
        n = len(rating)

        up, down = [0]*n, [0]*n

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if rating[i] > rating[j]:
                    up[i] += 1
                    res += up[j]
                else:
                    down[i] += 1
                    res += down[j]

        return res

    def numTeams_1(self, rating: List[int]) -> int:
        n = len(rating)

        @cache
        def dp_up(last: int, pos: int, k: int) -> int:
            if k == 0:
                return 1
            if pos == n:
                return 0
            resp = 0
            for i in range(pos, n):
                if rating[i] > last:
                    resp += dp_up(rating[i], i+1, k-1)
            return resp

        @cache
        def dp_down(last: int, pos: int, k: int) -> int:
            if k == 0:
                return 1
            if pos == n:
                return 0
            resp = 0
            for i in range(pos, n):
                if rating[i] < last:
                    resp += dp_down(rating[i], i+1, k-1)
            return resp

        return dp_up(-1, 0, 3) + dp_down(inf, 0, 3)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.numTeams(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 5, 3, 4, 1], 3)
    do_test(1, [2, 1, 3], 0)
    do_test(2, [1, 2, 3, 4], 4)

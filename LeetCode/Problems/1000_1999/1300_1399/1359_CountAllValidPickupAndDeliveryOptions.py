from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)

MOD = 10**9+7


class Solution:
    def countOrders(self, n: int) -> int:
        m = n*2
        resp = 1

        for _ in range(n-1):
            resp = (math.comb(m, 2) * resp) % MOD
            m -= 2

        return resp

    def countOrders_i(self, n: int) -> int:
        """internet_solution:
        https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/solutions/4024280/99-57-dp-math-recursion/?envType=daily-question&envId=2023-09-10
        """
        count = 1
        for i in range(2, n + 1):
            count = (count * (2 * i - 1) * i) % MOD
        return count


def do_test(i: int, s, r):
    c = Solution()
    resp = c.countOrders(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 1, 1)
    do_test(1, 2, 6)
    do_test(2, 3, 90)


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

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def countBits(self, n: int) -> List[int]:
        resp = [0] * (n+1)
        d = 1
        while d < n+1:
            for i in range(d, n+1, d*2):
                for j in range(i, min(n+1, i+d)):
                    resp[j] += 1
            d *= 2
        return resp

    def countBits_1(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n+1)]

    def countBits_i(self, n: int) -> List[int]:
        """internet solution:
        https://leetcode.com/problems/counting-bits/solutions/3986296/video-time-o-n-space-o-n-solution-with-python-javascript-java-and-c/?envType=daily-question&envId=2023-09-01
        """
        dp = [0] * (n + 1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i

            dp[i] = dp[i - sub] + 1

        return dp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.countBits(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, [0, 1, 1])
    do_test(1, 5, [0, 1, 1, 2, 1, 2])


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

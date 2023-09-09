from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def combinationSum4_i(self, nums: List[int], target: int) -> int:
        """internet solution:
        https://leetcode.com/problems/combination-sum-iv/solutions/4020218/98-22-dynamic-programming-recursion-with-memoization/?envType=daily-question&envId=2023-09-09
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def solve(rest: int) -> int:
            if rest < 0:
                return 0
            if rest == 0:
                return 1

            ans = 0
            for n in nums:
                ans += solve(rest - n)
            return ans

        return solve(target)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.combinationSum4(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3], 4, 7)
    do_test(1, [9], 3, 0)


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

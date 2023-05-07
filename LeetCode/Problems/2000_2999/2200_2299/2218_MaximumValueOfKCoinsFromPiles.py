from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        sp = [[0] * (k+1) for _ in range(len(piles))]

        for i in range(1, k+1):
            if len(piles[0]) >= i:
                sp[0][i] = sp[0][i-1] + piles[0][i-1]
            else:
                sp[0][i] = sp[0][i-1]

        for row in range(1, len(piles)):
            sums = [0]
            for i in range(1, k+1):
                if len(piles[row]) >= i:
                    sums.append(sums[i-1]+piles[row][i-1])

                for n, s in enumerate(sums):
                    if n > 0:
                        sp[row][i] = max(s, sp[row][i], sp[row-1][i-n] + sums[n])
                    else:
                        sp[row][i] = max(s, sp[row-1][i-n])

        return sp[-1][-1]

    def maxValueOfCoins_i(self, piles: List[List[int]], k: int) -> int:
        """sample solution 1"""
        n = len(piles)
        dp = [[0] * (k + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for coins in range(0, k + 1):
                current_sum = 0
                for current_coins in range(0, min(len(piles[i - 1]), coins) + 1):
                    if current_coins > 0:
                        current_sum += piles[i - 1][current_coins - 1]
                    dp[i][coins] = max(
                        dp[i][coins],
                        dp[i - 1][coins - current_coins] + current_sum
                    )
        return dp[n][k]

    def maxValueOfCoins_i(self, piles: List[List[int]], k: int) -> int:
        """sample solution 2"""
        n = len(piles)
        dp = [[-1] * (k + 1) for i in range(n + 1)]

        def f(i, coins):
            if i == 0:
                return 0
            if dp[i][coins] != -1:
                return dp[i][coins]
            current_sum = 0
            for current_coins in range(0, min(len(piles[i - 1]), coins) + 1):
                if current_coins > 0:
                    current_sum += piles[i - 1][current_coins - 1]
                dp[i][coins] = max(dp[i][coins],
                                   f(i - 1, coins - current_coins) + current_sum)
            return dp[i][coins]

        return f(n, k)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxValueOfCoins(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 100, 3], [7, 8, 9]], 2, 101)
    do_test(1, [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7, 706)
    do_test(2, [[1, 100, 3], [7, 8, 9]], 3, 108)
    do_test(3, [[1, 100, 3], [7, 8, 9]], 4, 116)
    do_test(4, [[100], [100], [1, 1, 1, 1, 1, 1, 700], [100], [100], [100], [100]], 7, 706)

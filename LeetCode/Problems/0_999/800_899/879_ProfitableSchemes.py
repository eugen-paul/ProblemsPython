from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        @cache
        def gr(rest_n: int, rest_min_pr: int, group_index) -> int:
            if rest_n <= 0 or group_index == len(group):
                return 0

            total = 0
            pr = profit[group_index] if rest_n >= group[group_index] else -2
            if pr >= rest_min_pr:
                total = 1
            a = rest_min_pr - profit[group_index]
            total += gr(rest_n - group[group_index], a if a >= 0 else -1, group_index + 1)
            total += gr(rest_n, rest_min_pr, group_index + 1)

            return total % 1000000007

        return (gr(n, minProfit, 0) + (1 if minProfit == 0 else 0)) % 1000000007

    def profitableSchemes_i1(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """sample solution"""
        mod = 1000000007
        memo = [[[-1 for _ in range(102)] for _ in range(102)] for _ in range(102)]

        def find(pos: int, count: int, profit: int, n: int, minProfit: int, group: List[int], profits: List[int]) -> int:
            if pos == len(group):
                # If profit exceeds the minimum required; it's a profitable scheme.
                return 1 if profit >= minProfit else 0

            if memo[pos][count][profit] != -1:
                # Repeated subproblem, return the stored answer.
                return memo[pos][count][profit]

            # Ways to get a profitable scheme without this crime.
            totalWays = find(pos + 1, count, profit, n, minProfit, group, profits)
            if count + group[pos] <= n:
                # Adding ways to get profitable schemes, including this crime.
                totalWays += find(pos + 1, count + group[pos], min(minProfit, profit + profits[pos]), n, minProfit, group, profits)

            memo[pos][count][profit] = totalWays % mod
            return memo[pos][count][profit]

        return find(0, 0, 0, n, minProfit, group, profit)

    def profitableSchemes_i2(self, n: int, minProfit: int, group: List[int], profits: List[int]) -> int:
        """sample solution"""
        mod = 1000000007

        dp = [[[0 for _ in range(102)] for _ in range(102)] for _ in range(102)]

        # Initializing the base case.
        for count in range(n+1):
            dp[len(group)][count][minProfit] = 1

        for index in range(len(group) - 1, -1, -1):
            for count in range(n+1):
                for profit in range(minProfit+1):
                    # Ways to get a profitable scheme without this crime.
                    dp[index][count][profit] = dp[index + 1][count][profit]
                    if count + group[index] <= n:
                        # Adding ways to get profitable schemes, including this crime.
                        a = dp[index][count][profit]
                        b = dp[index + 1][count + group[index]][min(minProfit, profit + profits[index])]
                        dp[index][count][profit] = (a+b) % mod

        return dp[0][0][0]


def do_test(i: int, s, n1, n2, n3, r):
    c = Solution()
    resp = c.profitableSchemes(s, n1, n2, n3)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 5, 3, [2, 2], [2, 3], 2)
    do_test(1, 10, 5, [2, 3, 5], [6, 7, 8], 7)
    do_test(2, 64, 0, [80, 40], [84, 84], 2)
    do_test(3, 1, 1,
            [1, 1, 1, 1, 2, 2, 1, 2, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 0, 2, 2],
            4)
    do_test(4, 95, 53,
            [82, 7, 18, 34, 1, 3, 83, 56, 50, 34, 39, 38, 76, 92, 71, 2, 6, 74, 1, 82, 22, 73, 88, 98, 6, 71, 6, 26, 100, 75, 57, 88, 43, 16, 22, 89, 7, 9, 78, 97, 22, 87, 34, 81,
                74, 56, 49, 94, 87, 71, 59, 6, 20, 66, 64, 37, 2, 42, 30, 87, 73, 16, 39, 87, 28, 9, 95, 78, 43, 59, 87, 78, 2, 93, 7, 22, 21, 59, 68, 67, 65, 63, 78, 20, 82, 35, 86],
            [45, 57, 38, 64, 52, 92, 31, 57, 31, 52, 3, 12, 93, 8, 11, 60, 55, 92, 42, 27, 40, 10, 77, 53, 8, 34, 87, 39, 8, 35, 28, 70, 32, 97, 88, 54, 82, 54, 54, 10, 78, 23, 82, 52,
                10, 49, 8, 36, 9, 52, 81, 26, 5, 2, 30, 39, 89, 62, 39, 100, 67, 33, 86, 22, 49, 15, 94, 59, 47, 41, 45, 17, 99, 87, 77, 48, 22, 77, 82, 85, 97, 66, 3, 38, 49, 60, 66],
            9883351)

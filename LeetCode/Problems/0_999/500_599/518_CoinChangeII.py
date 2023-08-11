from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [0] * (amount+1)
        coins = [c for c in coins if c <= amount]
        coins.sort()

        for c in coins:
            dp[c] += 1
            for a in range(c+1, amount+1):
                dp[a] += dp[a-c]

        return dp[-1]

    def change_s(self, amount: int, coins: List[int]) -> int:
        """sample solution"""
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] > j:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]

        return dp[0][amount]

    def change_s(self, amount: int, coins: List[int]) -> int:
        """sample solution"""
        def numberOfWays(i: int, amount: int) -> int:
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            if coins[i] > amount:
                memo[i][amount] = numberOfWays(i + 1, amount)
            else:
                memo[i][amount] = numberOfWays(i, amount - coins[i]) + numberOfWays(i + 1, amount)

            return memo[i][amount]

        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        return numberOfWays(0, amount)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.change(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 5, [1, 2, 5], 4)
    do_test(1, 3, [2], 0)
    do_test(2, 10, [10], 1)
    do_test(3, 6, [1, 2, 5], 5)
    do_test(4, 7, [1, 2, 5], 6)

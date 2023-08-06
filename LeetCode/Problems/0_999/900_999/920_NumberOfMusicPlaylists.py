from collections import defaultdict
from functools import cache
import itertools
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def numMusicPlaylists_s(self, n: int, goal: int, k: int) -> int:
        """sample solution"""
        MOD = 10**9 + 7

        # Initialize the DP table
        dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                # The i-th song is a new song
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % MOD
                # The i-th song is a song we have played before
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD

        return dp[goal][n]


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.numMusicPlaylists(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 3, 1, 6)
    do_test(1, 2, 3, 0, 6)
    do_test(2, 2, 3, 1, 2)
    do_test(3, 3, 4, 1, 18)

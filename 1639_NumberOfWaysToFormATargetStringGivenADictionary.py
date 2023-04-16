from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dp = [[0] * (len(words[0]) + 1) for _ in range(len(target) + 1)]

        for i in range(len(words[0]) + 1):
            dp[0][i] = 1

        @cache
        def get_count(c: str, i: int) -> int:
            cnt = 0
            for w in words:
                if w[i] == c:
                    cnt += 1
            return cnt

        for pos, c in enumerate(target):
            for i in range(pos, len(words[0]) - len(target) + pos + 1):
                cnt = get_count(c, i)
                dp[pos + 1][i + 1] = (cnt * dp[pos][i] + dp[pos + 1][i]) % 1000000007
        return dp[-1][-1]

    def numWays_1(self, words: List[str], target: str) -> int:
        dp = [[0] * (len(words[0]) + 1) for _ in range(len(target) + 1)]

        for i in range(len(words[0]) + 1):
            dp[0][i] = 1

        for pos, c in enumerate(target):
            for i in range(pos, len(words[0]) - len(target) + pos + 1):
                cnt = 0
                for w in words:
                    if w[i] == c:
                        cnt += 1
                dp[pos + 1][i + 1] = (cnt * dp[pos][i] + dp[pos + 1][i]) % 1000000007
        return dp[-1][-1]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.numWays(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        "acca",
        "bbbb",
        "caca"
    ],
        "aba", 6)
    do_test(1, ["abba", "baab"], "bab", 4)

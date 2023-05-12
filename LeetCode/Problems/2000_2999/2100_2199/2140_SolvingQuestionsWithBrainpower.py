from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions)+1)

        for i in range(len(questions)-1, -1, -1):
            p, b = questions[i]
            if i+b >= len(questions):
                dp[i] = max(p, dp[i+1])
            else:
                dp[i] = max(p + dp[i+b+1], dp[i+1])
        return dp[0]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.mostPoints(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[3, 2], [4, 3], [4, 4], [2, 5]], 5)
    do_test(1, [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7)
    do_test(2, [[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]], 79)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def max_sub(p1: int, p2: int) -> int:
            if len(nums1) == p1 or len(nums2) == p2:
                return 0

            v2 = nums2[p2]
            a = -inf
            try:
                f = nums1.index(v2, p1)
                a = max_sub(f+1, p2+1)
            except ValueError:
                pass
            b = max_sub(p1, p2+1)
            return max(a+1, b)

        return max_sub(0, 0)

    def maxUncrossedLines_i(self, nums1, nums2):
        """sample solution"""
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n1][n2]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxUncrossedLines(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 4, 2], [1, 2, 4], 2)
    do_test(1, [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3)
    do_test(2, [1, 3, 7, 1, 7, 5],  [1, 9, 2, 5, 1], 2)
    do_test(3, [1, 2, 3, 4, 5, 6],  [1, 2, 3, 4, 5, 6], 6)
    do_test(4, [1],  [2], 0)

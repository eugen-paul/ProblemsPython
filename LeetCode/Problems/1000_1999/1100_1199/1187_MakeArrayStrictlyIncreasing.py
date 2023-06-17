import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def makeArrayIncreasing_s(self, arr1: List[int], arr2: List[int]) -> int:
        """sample solution"""
        dp = {}
        arr2.sort()

        def dfs(i, prev):
            if i == len(arr1):
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]

            cost = float('inf')

            # If arr1[i] is already greater than prev, we can leave it be.
            if arr1[i] > prev:
                cost = dfs(i + 1, arr1[i])

            # Find a replacement with the smallest value in arr2.
            idx = bisect.bisect_right(arr2, prev)

            # Replace arr1[i], with a cost of 1 operation.
            if idx < len(arr2):
                cost = min(cost, 1 + dfs(i + 1, arr2[idx]))

            dp[(i, prev)] = cost
            return cost

        res = dfs(0, -1)

        return res if res < float('inf') else -1

    def makeArrayIncreasing_s(self, arr1: List[int], arr2: List[int]) -> int:
        """sample solution"""
        dp = {-1: 0}
        arr2.sort()
        n = len(arr2)

        for i in range(len(arr1)):
            new_dp = defaultdict(lambda: float('inf'))
            for prev in dp:
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
                idx = bisect.bisect_right(arr2, prev)
                if idx < n:
                    new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])
            dp = new_dp

        return min(dp.values()) if dp else -1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.makeArrayIncreasing(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 5, 3, 6, 7],  [1, 3, 2, 4], 1)
    do_test(1, [1, 5, 3, 6, 7],  [4, 3, 1], 2)
    do_test(2, [1, 5, 3, 6, 7],  [1, 6, 3, 3], -1)
    do_test(3, [5, 3, 6, 7],  [1, 3, 2, 4], 1)
    do_test(4, [0, 11, 6, 1, 4, 3],  [5, 4, 11, 10, 1, 0], 5)

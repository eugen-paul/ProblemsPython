import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        starts = [s[0] for s in intervals]

        dp = [-1] * len(intervals)

        def solve(pos: int) -> int:
            if pos == len(intervals):
                return 0
            if dp[pos] != -1:
                return dp[pos]

            end = intervals[pos][1]
            nxt = bisect.bisect_left(starts, end)
            resp = nxt - pos - 1 + solve(nxt)
            resp = min(resp, solve(pos+1) + 1)

            dp[pos] = resp
            return resp

        return solve(0)

    def eraseOverlapIntervals_s(self, intervals: List[List[int]]) -> int:
        """sample solution"""
        intervals.sort(key=lambda x: x[1])
        ans = 0
        k = -inf

        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ans += 1

        return ans


def do_test(i: int, s, r):
    c = Solution()
    resp = c.eraseOverlapIntervals(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 2], [2, 3], [3, 4], [1, 3]], 1)
    do_test(1, [[1, 2], [1, 2], [1, 2]], 2)
    do_test(2, [[1, 2], [2, 3]], 0)
    do_test(3, [[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]], 4)

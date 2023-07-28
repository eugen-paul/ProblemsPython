from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def solve(l: int, r: int) -> int:
            if l > r:
                return 0

            s = sum(nums[l:r+1])

            return max(
                s - solve(l+1, r),
                s - solve(l, r-1)
            )

        score_p1 = solve(0, len(nums)-1)

        return score_p1 * 2 >= sum(nums)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.PredictTheWinner(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 5, 2], False)
    do_test(1, [1, 5, 233, 7], True)
    do_test(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True)

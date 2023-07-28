from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        def is_ok(t: int) -> bool:
            delta = 0
            for b in batteries:
                if t > b:
                    delta += b
                else:
                    delta += t
            return delta // n >= t

        l, r = 0, sum(batteries)
        while l < r:
            m = (r+l+1)//2
            if is_ok(m):
                l = m
            else:
                r = m-1
        return l

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """internet solution"""
        # Get the sum of all extra batteries.
        batteries.sort()
        extra = sum(batteries[:-n])

        # live stands for the n largest batteries we chose for n computers.
        live = batteries[-n:]

        # We increase the total running time using 'extra' by increasing
        # the running time of the computer with the smallest battery.
        for i in range(n - 1):
            # If the target running time is between live[i] and live[i + 1].
            if extra // (i + 1) < live[i + 1] - live[i]:
                return live[i] + extra // (i + 1)

            # Reduce 'extra' by the total power used.
            extra -= (i + 1) * (live[i + 1] - live[i])

        # If there is power left, we can increase the running time
        # of all computers.
        return live[-1] + extra // n


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxRunTime(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, 2, [3, 3, 3], 4)
    # do_test(1, 2, [1, 1, 1, 1], 2)
    # do_test(2, 1, [1, 2, 3, 4], 10)
    do_test(3, 2, [1, 2, 10], 3)

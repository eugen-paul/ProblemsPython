import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        sum_pos = 0
        resp = 0

        for n in reversed(satisfaction):
            if -n > sum_pos:
                break
            resp += n + sum_pos
            sum_pos += n

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxSatisfaction(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [-1, -8, 0, 5, -9], 14)
    do_test(1, [4, 3, 2], 20)
    do_test(2, [-1, -4, -5], 0)

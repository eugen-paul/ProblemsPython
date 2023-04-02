import bisect
from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        resp = []
        for n in spells:
            mlt = math.ceil(success / n)
            sp = bisect.bisect_left(potions, mlt)
            resp.append(len(potions)-sp)
        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.successfulPairs(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [5, 1, 3], [1, 2, 3, 4, 5], 7, [4, 0, 3])
    do_test(1, [3, 1, 2], [8, 5, 8], 16, [2, 0, 2])

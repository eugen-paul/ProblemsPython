from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        s = set(nums)

        for f, t in zip(moveFrom, moveTo):
            s.discard(f)
            s.add(t)

        return sorted(s)


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.relocateMarbles(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 6, 7, 8],  [1, 7, 2],  [2, 9, 5], [5, 6, 8, 9])
    do_test(1, [1, 1, 3, 3],  [1, 3],  [2, 2], [2])

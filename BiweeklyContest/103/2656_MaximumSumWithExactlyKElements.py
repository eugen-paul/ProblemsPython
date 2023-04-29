from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        return sum (range(m, m+k))


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maximizeSum(s,n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4, 5], 3, 18)

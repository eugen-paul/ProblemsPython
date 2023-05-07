from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findKthLargest(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 2, 1, 5, 6, 4], 2, 5)
    do_test(1, [3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        resp = [k for k, _ in c.most_common(k)]
        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.topKFrequent(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 1, 1, 2, 2, 3], 2, [1, 2])
    do_test(1, [1], 1, [1])

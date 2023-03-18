from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        count = Counter(nums)

        resp = len(nums)
        max_count = count.most_common(1)[0]
        count.pop(max_count[0])
        resp -= max_count[1]

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maximizeGreatness(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 5, 2, 1, 3, 1], 4)
    do_test(0, [1, 2, 3, 4], 3)

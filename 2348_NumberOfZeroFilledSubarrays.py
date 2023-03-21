from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        resp = 0

        count = 0
        for n in nums:
            if n == 0:
                count += 1
            else:
                resp += (count * (count+1) // 2)
                count = 0
        resp += (count * (count+1) // 2)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.zeroFilledSubarray(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, [1, 3, 0, 0, 2, 0, 0, 4], 6)
    do_test(0, [0, 0, 0, 2, 0, 0], 9)
    do_test(0, [2, 10, 2019], 0)

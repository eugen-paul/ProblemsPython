from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        resp = -1

        for i in range(n):
            for j in range(i+1, n):
                if (j-i) % 2 == 1 and nums[j] != nums[i]+1:
                    break
                if (j-i) % 2 == 0 and nums[j] != nums[i]:
                    break
                resp = max(resp, j-i+1)
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.alternatingSubarray(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, 4, 3, 4], 4)
    do_test(1, [4, 5, 6], 2)
    do_test(1, [2, 5], -1)
    do_test(2, [2, 3], 2)

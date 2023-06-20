from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        resp = [-1] * len(nums)

        cur = 0
        cnt = 0
        for i, n in enumerate(nums):
            cur += n
            cnt += 1
            if cnt == 2*k+1:
                resp[i-k] = cur // cnt
                cnt -= 1
                cur -= nums[i-2*k]

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.getAverages(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [7, 4, 3, 9, 1, 8, 5, 2, 6], 3, [-1, -1, -1, 5, 4, 4, -1, -1, -1])
    do_test(1, [100000], 0, [100000])
    do_test(2, [8], 100000, [-1])

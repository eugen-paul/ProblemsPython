from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()

        if nums[0] > 0:
            resp = 1
            for i in nums:
                resp *= i
            return resp

        nul = [x for x in nums if x == 0]
        neg = [x for x in nums if x < 0]
        pos = [x for x in nums if x > 0]

        nums = [x for x in nums if x != 0]

        if len(neg) == 1 and len(pos) == 0:
            if len(nul) == 0:
                return neg[0]
            return 0

        if len(neg) == 0 and len(pos) == 0:
            return 0

        resp = 1
        for i in neg:
            resp *= i
        for i in pos:
            resp *= i
        if len(neg) % 2 == 1:
            resp //= neg[-1]
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxStrength(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, -1, -5, 2, 5, -9], 1350)
    do_test(1, [-4, -5, -4], 20)
    do_test(2, [-4], -4)
    do_test(3, [-4, 0], 0)
    do_test(4, [-4, -3], 12)
    do_test(5, [-4, -3, 2], 24)
    do_test(6, [0], 0)

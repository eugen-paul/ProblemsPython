from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """internet solution"""
        num1, num2 = None, None
        cnt1, cnt2 = 0, 0

        for c in nums:
            if c == num1:
                cnt1 += 1
            elif c == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = c
                cnt1 = 1
            elif cnt2 == 0:
                num2 = c
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = nums.count(num1), nums.count(num2)

        n = len(nums)
        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3 and num2 != num1:
            res.append(num2)

        return res

    def majorityElement_1(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        c = Counter(nums)
        resp = []
        for k, v in c.items():
            if v > limit:
                resp.append(k)
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.majorityElement(s)
    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 2, 3], [3])
    do_test(1, [1], [1])
    do_test(2, [1, 2], [1, 2])
    do_test(3, [1, 2, 3], [])
    do_test(4, [0, 3, 4, 0], [0])
    do_test(5, [2, 2, 1, 3], [2])

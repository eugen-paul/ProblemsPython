from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resp = [nums[-1]]
        for i in range(1, len(nums)):
            resp.append(resp[i-1] * nums[-i-1])
        resp.reverse()

        l = 1
        for i in (range(len(nums)-1)):
            resp[i] = resp[i+1] * l
            l *= nums[i]
        resp[-1] = l
        return resp

    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        l = [1]
        for i in range(len(nums)):
            l.append(l[i] * nums[i])

        r = [1]
        for i in range(len(nums)):
            r.append(r[i] * nums[-i-1])
        r.reverse()

        resp = []
        for i in (range(len(nums))):
            resp.append(l[i] * r[i+1])
        return resp

    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        cnt = nums.count(0)

        resp = []
        if cnt == 0:
            pr = 1
            for n in nums:
                pr *= n
            for n in nums:
                resp.append(pr // n)
        elif cnt == 1:
            pos = nums.index(0)
            pr = 1
            for n in nums:
                if n != 0:
                    pr *= n
            for i in range(len(nums)):
                if i != pos:
                    resp.append(0)
                else:
                    resp.append(pr)
        else:
            for i in range(len(nums)):
                resp.append(0)
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.productExceptSelf(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4], [24, 12, 8, 6])
    do_test(1, [-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
    do_test(2, [-1, 1, 0, 0, 3], [0, 0, 0, 0, 0])

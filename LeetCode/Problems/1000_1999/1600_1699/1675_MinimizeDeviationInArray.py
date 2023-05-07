import heapq
from math import inf
from typing import List, Dict, Tuple, Counter
import bisect


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        s = []
        min_val = inf
        nums.sort()
        last = -1
        for n in nums:
            if last == n:
                continue
            last = n
            if n & 1 == 1:
                n = n*2
            heapq.heappush(s, -n)
            min_val = min(min_val, n)

        min_delta = inf
        while True:
            nxt = -heapq.heappop(s)
            min_delta = min(min_delta, nxt - min_val)
            if nxt & 1 == 1:
                break
            nxt = nxt // 2
            min_val = min(min_val, nxt)
            heapq.heappush(s, -nxt)

        return min_delta

    def minimumDeviation_1(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n & 1 == 1:
                nums[i] = n*2

        nums = sorted(set(nums))
        min_delta = nums[-1] - nums[0]

        while nums[-1] & 1 == 0:
            t = nums.pop()
            bisect.insort_right(nums, t // 2)
            min_delta = min(min_delta, nums[-1] - nums[0])

        return min_delta


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minimumDeviation(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4], 1)
    do_test(1, [4, 1, 5, 20, 3], 3)
    do_test(2, [2, 10, 8], 3)
    do_test(3, [1, 32], 0)
    do_test(4, [1, 64], 0)
    do_test(5, [65, 64], 1)
    do_test(6, [65, 2], 63)
    do_test(7, [65, 1], 63)
    do_test(8, [65, 129], 1)
    do_test(9, [65, 145], 15)
    do_test(10, [11, 20, 18], 2)
    do_test(11, [3, 3, 3, 16], 1)
    do_test(12, [3, 1, 16], 1)
    do_test(13, [3, 3, 3, 3, 3, 1, 1, 16], 1)

import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        srt = sorted(nums[:indexDiff+1])

        last = srt[0]
        for i in range(1, len(srt)):
            cur = srt[i]
            if cur - last <= valueDiff:
                return True
            last = cur

        for start in range(1, len(nums) - indexDiff):
            first = nums[start-1]
            pos = bisect.bisect_left(srt, first)
            srt.pop(pos)

            cur = nums[start + indexDiff]
            pos = bisect.bisect_left(srt, cur)
            if pos > 0 and cur - srt[pos-1] <= valueDiff:
                return True
            if pos < len(srt) and srt[pos]-cur <= valueDiff:
                return True
            bisect.insort(srt, cur)

        return False

    def containsNearbyAlmostDuplicate_i(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        """internet solution:
        https://leetcode.com/problems/contains-duplicate-iii/solutions/2298891/two-python-solutions-memory-optimization-speed-optimization/
        """
        if not nums or indexDiff <= 0 or valueDiff < 0:
            return False

        mini = min(nums)
        diff = valueDiff + 1  # In case of valueDiff = 0
        bucket = {}

        def getKey(num: int) -> int:
            return (num - mini) // diff

        for i, num in enumerate(nums):
            key = getKey(num)
            if key in bucket:  # Current bucket
                return True
            # Left adjacent bucket
            if key - 1 in bucket and num - bucket[key - 1] < diff:
                return True
            # Right adjacent bucket
            if key + 1 in bucket and bucket[key + 1] - num < diff:
                return True
            bucket[key] = num
            if i >= indexDiff:
                del bucket[getKey(nums[i - indexDiff])]

        return False


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.containsNearbyAlmostDuplicate(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, [1, 2, 3, 1], 3, 0, True)
    # do_test(1, [1, 5, 9, 1, 5, 9], 2, 3, False)
    do_test(2, [1, 5, 9, 1, 5, 9], 2, 1, False)
    do_test(3, [1, 5, 9, 1, 5, 9, 10], 2, 3, True)
    do_test(4, [1, 2, 1, 1], 1, 0, True)

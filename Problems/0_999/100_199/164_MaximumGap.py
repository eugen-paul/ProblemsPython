from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        last = nums[0]
        resp = 0
        for n in nums:
            resp = max(resp, n - last)
            last = n
        return resp

    def maximumGap_i(self, nums: List[int]) -> int:
        """internet solution"""

        # Check if the list is empty or contains only one element
        if len(nums) < 2:
            return 0

        # Get the minimum and maximum values in the list
        min_val = min(nums)
        max_val = max(nums)

        # Calculate the bucket size and number of buckets
        bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
        num_buckets = (max_val - min_val) // bucket_size + 1

        # Initialize the buckets
        buckets = [None] * num_buckets

        # Put each element in its corresponding bucket
        for num in nums:
            bucket_index = (num - min_val) // bucket_size
            if not buckets[bucket_index]:
                buckets[bucket_index] = {'min': num, 'max': num}
            else:
                buckets[bucket_index]['min'] = min(buckets[bucket_index]['min'], num)
                buckets[bucket_index]['max'] = max(buckets[bucket_index]['max'], num)

        # Calculate the maximum gap between adjacent buckets
        max_gap = 0
        prev_max = min_val
        for bucket in buckets:
            if bucket:
                max_gap = max(max_gap, bucket['min'] - prev_max)
                prev_max = bucket['max']

        return max_gap


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maximumGap(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 6, 9, 1], 3)
    do_test(1, [10], 0)
    do_test(2, [3, 6, 20, 1], 14)
    do_test(3, [2, 1, 4, 3], 1)

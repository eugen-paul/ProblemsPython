from collections import defaultdict
from functools import cache
from math import gcd, inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        """using help"""

        def comp_diff(bucket: List[int]) -> int:
            resp = 0
            bucket.sort()
            median = bucket[len(bucket) // 2]
            for n in bucket:
                resp += abs(median-n)
            return resp

        resp = 0
        for i in range(len(arr)):
            bucket = []
            pos = i
            while arr[pos] != 0:
                bucket.append(arr[pos])
                arr[pos] = 0
                pos = (pos+k) % len(arr)
            if bucket:
                resp += comp_diff(bucket)

        return resp

    def makeSubKSumEqual_i2(self, arr: List[int], k: int) -> int:
        """internet solution"""
        g = gcd(len(arr), k)
        resp = 0
        for i in range(g):
            bucket = []
            for j in range(i, len(arr), g):
                bucket.append(arr[j])
            bucket.sort()
            median = bucket[len(bucket) // 2]
            for n in bucket:
                resp += abs(median-n)

        return resp

    def makeSubKSumEqual_i(self, arr: List[int], k: int) -> int:
        """internet solution"""
        """https://leetcode.com/problems/make-k-subarray-sums-equal/solutions/3367765/explaining-like-you-are-five-years-old/"""

        n = len(arr)

        no_of_buckets = gcd(k, n)
        buckets = defaultdict(list)

        for ind, num in enumerate(arr):
            buckets[ind % no_of_buckets].append(num)

        result = 0
        for bucket_number, bucket in buckets.items():
            sorted_bucket = sorted(bucket)
            m = len(sorted_bucket)
            median = sorted_bucket[(m)//2]

            for num in bucket:
                result += abs(median - num)

        return result

    def makeSubKSumEqual_1(self, arr: List[int], k: int) -> int:
        """!WRONG!"""
        s = sum(arr[:k])
        sub_sums = [s]
        for i in range(k, len(arr)):
            s -= arr[i-k]
            s += arr[i]
            sub_sums.append(s)
        for i in range(k-1):
            s -= arr[len(arr) - k + i]
            s += arr[i]
            sub_sums.append(s)

        m = math.ceil(sum(sub_sums) / len(sub_sums))

        resp = 0
        pos = 0
        while pos < len(sub_sums):
            delta = m-sub_sums[pos]
            resp += abs(delta)
            for i in range(1, k):
                sub_sums[pos - i] += delta
            pos += k

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.makeSubKSumEqual(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 4, 1, 3], 2, 1)
    do_test(1, [2, 5, 5, 7], 3, 5)
    do_test(2, [2, 10, 9], 1, 8)

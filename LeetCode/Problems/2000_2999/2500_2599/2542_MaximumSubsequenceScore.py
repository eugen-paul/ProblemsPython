from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        s = sorted(zip(nums2, nums1), reverse=True)
        q = []

        sumN1 = 0
        heapq.heapify(q)
        resp = 0

        for n2, n1 in s:
            sumN1 += n1
            heapq.heappush(q, n1)
            if len(q) > k:
                sm = heapq.heappop(q)
                sumN1 -= sm
            if len(q) == k:
                resp = max(resp, sumN1 * n2)
        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.maxScore(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 3, 2],  [2, 1, 3, 4], 3, 12)
    do_test(1, [4, 2, 3, 1, 1],  [7, 5, 10, 9, 6], 1, 30)

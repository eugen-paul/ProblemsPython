from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        tmp = []
        heapq.heapify(tmp)

        for a in nums1:
            for b in nums2:
                if len(tmp) == k and -a-b < tmp[0][0]:
                    break
                heapq.heappush(tmp, (-a-b, a))
                if len(tmp) > k:
                    heapq.heappop(tmp)

        resp = []
        for _ in range(min(k, len(tmp))):
            d = heapq.heappop(tmp)
            resp.append([d[1], -d[1]-d[0]])

        return resp[::-1]

    def kSmallestPairs_s(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """sample solution"""
        from heapq import heappush, heappop
        m = len(nums1)
        n = len(nums2)

        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))

        while k > 0 and minHeap:
            _, (i, j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k = k - 1

        return ans

    def kSmallestPairs_t(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """Time Limit Exceeded"""
        tmp = []
        heapq.heapify(tmp)

        for a in nums1:
            for b in nums2:
                heapq.heappush(tmp, (-a-b, a))
                if len(tmp) > k:
                    heapq.heappop(tmp)

        resp = []
        for _ in range(min(k, len(tmp))):
            d = heapq.heappop(tmp)
            resp.append([d[1], -d[1]-d[0]])

        return resp[::-1]

    def kSmallestPairs_m(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """memory Limit Exceeded"""
        tmp = []
        heapq.heapify(tmp)

        for a in nums1:
            for b in nums2:
                heapq.heappush(tmp, (a+b, a, b))

        resp = []
        for _ in range(min(k, len(tmp))):
            d = heapq.heappop(tmp)
            resp.append([d[1], d[2]])

        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.kSmallestPairs(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]])
    do_test(1, [1, 1, 2], [1, 2, 3], 2, [[1, 1], [1, 1]])
    do_test(2, [1, 2], [3], 3, [[1, 3], [2, 3]])
    # do_test(3, [i for i in range(1, 10001)], [i for i in range(1, 10001)], 10000, [[1, 3], [2, 3]])

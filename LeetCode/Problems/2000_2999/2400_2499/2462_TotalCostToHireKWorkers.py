from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if n <= candidates * 2:
            return sum(sorted(costs)[:k])

        q = []
        heapq.heapify(q)

        for i in range(candidates):
            heapq.heappush(q, (costs[i], i))
            heapq.heappush(q, (costs[n-i-1], n-i-1))

        l, r = candidates-1, n-candidates
        resp = 0
        for i in range(k):
            sm = heapq.heappop(q)
            resp += sm[0]
            pos = sm[1]
            if l+1 < r and pos <= l:
                l += 1
                heapq.heappush(q, (costs[l], l))

            if l < r-1 and pos >= r:
                r -= 1
                heapq.heappush(q, (costs[r], r))

        return resp

    def totalCost_1(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        q = []
        heapq.heapify(q)

        for i in range(candidates):
            heapq.heappush(q, (costs[i], i))
            heapq.heappush(q, (costs[n-i-1], n-i-1))

        resp = 0
        l, r = candidates-1, n-candidates
        for i in range(k):
            sm = heapq.heappop(q)
            if sm == q[0]:
                heapq.heappop(q)
            resp += sm[0]
            pos = sm[1]
            costs[pos] = -1
            if pos <= l:
                l += 1
                while l < len(costs) and costs[l] == -1:
                    l += 1
                if l < len(costs):
                    heapq.heappush(q, (costs[l], l))

            if pos >= r:
                r -= 1
                while r >= 0 and costs[r] == -1:
                    r -= 1
                if r >= 0:
                    heapq.heappush(q, (costs[r], r))

        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.totalCost(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4, 11)
    do_test(1, [1, 2, 4, 1], 3, 3, 4)
    do_test(2, [1, 2, 3], 3, 3, 6)
    do_test(3, [28, 35, 21, 13, 21, 72, 35, 52, 74, 92, 25, 65, 77, 1, 73, 32, 43, 68, 8, 100,
            84, 80, 14, 88, 42, 53, 98, 69, 64, 40, 60, 23, 99, 83, 5, 21, 76, 34], 32, 12, 1407)

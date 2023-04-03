from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        resp = 0

        l, r = 0, len(people)-1
        while l <= r:
            if people[r] + people[l] <= limit:
                l += 1
            r -= 1
            resp += 1

        return resp

    def numRescueBoats_1(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        resp = 0

        rest = []
        heapq.heapify(rest)

        for n in people:
            if len(rest) == 0 or -rest[0] < n:
                resp += 1
                heapq.heappush(rest, -(limit - n))
            else:
                heapq.heappop(rest)

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.numRescueBoats(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2], 3, 1)
    do_test(1, [3, 2, 2, 1], 3, 3)
    do_test(2, [3, 5, 3, 4], 5, 4)
    do_test(3, [1, 2, 3, 4], 5, 2)
    do_test(4, [3, 2, 3, 2, 2], 6, 3)
    do_test(5, [5, 5, 5, 5, 5], 5, 5)
    do_test(6, [5, 5, 5, 5], 5, 4)

from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rev = [-n for n in stones]
        heapq.heapify(rev)

        while rev:
            if len(rev) == 1:
                return -rev[0]
            t1 = heapq.heappop(rev)
            t2 = heapq.heappop(rev)
            if t1 != t2:
                heapq.heappush(rev, t1 - t2)
        return 0


def do_test(i: int, s, r):
    c = Solution()
    resp = c.lastStoneWeight(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 7, 4, 1, 8, 1], 1)
    do_test(1, [1], 1)

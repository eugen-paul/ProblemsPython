from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findScore(self, nums: List[int]) -> int:
        m: Dict[int, List[int]] = defaultdict(list)
        marked: List[bool] = [False] * len(nums)
        q = []
        heapq.heapify(q)

        for i, n in enumerate(nums):
            heapq.heappush(q, n)
            m[n].append(i)

        resp = 0
        while q:
            next_val = heapq.heappop(q)
            next_pos = m[next_val].pop(0)
            if marked[next_pos]:
                continue
            resp += next_val
            marked[next_pos] = True
            if next_pos+1 < len(nums):
                marked[next_pos+1] = True
            if next_pos-1 >= 0:
                marked[next_pos-1] = True

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findScore(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 1, 3, 4, 5, 2], 7)
    do_test(0, [2, 3, 5, 1, 3, 2], 5)

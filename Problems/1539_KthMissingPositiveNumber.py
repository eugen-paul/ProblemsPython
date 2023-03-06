from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss_count = 0
        pos = 0
        resp = 1
        while True:
            if pos >= len(arr):
                return resp+k-miss_count-1
            while pos < len(arr) and arr[pos] > resp:
                miss_count += 1
                if miss_count == k:
                    return resp
                resp += 1
            pos += 1
            resp += 1

    def findKthPositive_1(self, arr: List[int], k: int) -> int:
        s = set(arr)
        resp = 0
        miss = 0
        for i in range(1, 2002):
            if i not in s:
                miss += 1
                resp = i
                if miss == k:
                    break

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findKthPositive(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, 4, 7, 11], 5, 9)
    do_test(1, [1, 2, 3, 4], 2, 6)
    do_test(2, [2], 1, 1)
    do_test(3, [1], 1, 2)
    do_test(4, [1], 2, 3)

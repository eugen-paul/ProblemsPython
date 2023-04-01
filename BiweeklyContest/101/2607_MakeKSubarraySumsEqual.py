from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        # TODO
        pass

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

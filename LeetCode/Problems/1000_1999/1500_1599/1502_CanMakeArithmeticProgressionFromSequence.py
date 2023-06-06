from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1]-arr[0]
        for i in range(2, len(arr)):
            if arr[i]-arr[i-1] != d:
                return False
        return True

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n, mi, ma = len(arr), min(arr), max(arr)

        if ma == mi:
            return True

        if (ma - mi) % (n-1) != 0:
            return False

        d = (ma - mi) // (n-1)
        a = [0] * n
        for c in arr:
            if (c-mi) % d != 0:
                return False
            a[(c-mi) // d] = 1

        return min(a) == 1


def do_test(i: int, s, r):
    c = Solution()
    resp = c.canMakeArithmeticProgression(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 5, 1], True)
    do_test(1, [1, 2, 4], False)
    do_test(2, [1, 1], True)
    do_test(3, [1, 1, 1, 1], True)

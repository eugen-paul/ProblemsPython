from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        as_str = "0" + "".join(str(x) for x in flowerbed) + "0"
        parts = as_str.split("1")
        resp = 0
        for p in parts:
            resp += (len(p)-1) // 2
        return resp >= n

    def canPlaceFlowers_1(self, flowerbed: List[int], n: int) -> bool:
        empty_count = 1
        flowers = 0
        for i in flowerbed:
            if i == 0:
                empty_count += 1
                if empty_count == 3:
                    empty_count = 1
                    flowers += 1
            else:
                empty_count = 0

        if empty_count == 2:
            flowers += 1

        return flowers >= n


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.canPlaceFlowers(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 0, 0, 0, 1], 1, True)
    do_test(1, [1, 0, 0, 0, 1], 2, False)
    do_test(2, [0, 0, 1, 0, 0], 2, True)
    do_test(3, [0, 0, 1], 1, True)
    do_test(4, [1, 0, 0], 1, True)
    do_test(5, [0, 1], 1, False)
    do_test(6, [1, 0], 1, False)
    do_test(7, [1, 0, 0, 0, 0, 1], 2, False)
    do_test(8, [1, 0, 0, 0, 0, 0, 1], 2, True)
    do_test(9, [1, 0, 0, 0, 0, 0, 0, 0, 1], 3, True)
    do_test(10, [1, 0, 0, 0, 0, 0, 0, 0, 1], 4, False)

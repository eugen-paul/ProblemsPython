from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie
        a = round(math.log(buckets, rounds+1), 8)
        return math.ceil(a)

    def poorPigs_1(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        rounds = minutesToTest // minutesToDie

        if rounds == 1:
            a = math.log2(buckets)
            return math.ceil(a)
        a = round(math.log(buckets, rounds+1), 8)
        return math.ceil(a)


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.poorPigs(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(1, 1, 15, 15, 0)
    do_test(2, 2, 15, 15, 1)
    do_test(3, 3, 15, 15, 2)
    do_test(4, 4, 15, 15, 2)
    do_test(5, 5, 15, 15, 3)
    do_test(6, 6, 15, 15, 3)
    do_test(7, 7, 15, 15, 3)
    do_test(8, 8, 15, 15, 3)
    do_test(9, 9, 15, 15, 4)
    do_test(10, 10, 15, 15, 4)
    do_test(11, 11, 15, 15, 4)
    do_test(12, 4, 15, 30, 2)
    do_test(13, 14, 3, 98, 1)
    do_test(14, 14, 23, 98, 2)
    do_test(15, 1000, 15, 60, 5)
    do_test(16, 8, 15, 40, 2)
    do_test(17, 125, 1, 4, 3)

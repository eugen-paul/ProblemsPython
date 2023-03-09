from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = [1] * len(ratings)
        r = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] == ratings[i]:
                l[i] = 1
            elif ratings[i-1] >= ratings[i]:
                l[i] = 1
            else:
                l[i] = l[i-1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i+1] == ratings[i]:
                r[i] = 1
            elif ratings[i+1] >= ratings[i]:
                r[i] = 1
            else:
                r[i] = r[i+1] + 1

        resp = sum([max(a, b) for a, b in zip(l, r)])
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.candy(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 0, 2], 5)
    do_test(1, [1, 2, 2], 4)
    do_test(2, [1, 2, 3], 6)
    do_test(3, [3, 2, 1], 6)
    do_test(4, [2, 2, 2], 3)
    do_test(5, [1, 2, 3, 1, 2, 3], 12)
    do_test(6, [3, 2, 1, 3, 2, 1], 12)

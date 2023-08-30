from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = inf
        cnt = 0
        for n in reversed(nums):
            if n <= last:
                last = n
                continue
            r = n // last
            if n % last == 0:
                cnt += r - 1
            else:
                cnt += r
                last = n // (r + 1)
        return cnt


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minimumReplacement(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 9, 3], 2)
    do_test(1, [1, 2, 3, 4, 5], 0)
    do_test(2, [12, 9, 7, 6, 17, 19, 21], 6)
    do_test(3, [7, 6, 15, 6, 11, 14, 10], 10)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

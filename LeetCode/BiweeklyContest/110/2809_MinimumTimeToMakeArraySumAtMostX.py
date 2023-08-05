from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minimumTime_w(self, nums1: List[int], nums2: List[int], x: int) -> int:
        """wrong :("""
        def is_ok(n) -> bool:
            r = [(a[0]+a[1]*n, i) for i, a in enumerate(zip(nums1, nums2))]
            r.sort(reverse=True, key=lambda x: (x[0], nums2[x[1]]))
            for i in range(n):
                r[i] = (nums2[r[i][1]] * i, 0)
            s = 0
            for i in r:
                s += i[0]

            return s <= x

        l, r = 0, len(nums1)+1
        while l <= r and l <= len(nums1):
            m = (r+l)//2
            if is_ok(m):
                r = m-1
            else:
                l = m+1

        return l if l <= len(nums1) else -1


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.minimumTime(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, [1, 2, 3], [1, 2, 3], 4, 3)
    # do_test(1, [1, 2, 3], [3, 3, 3], 4, -1)
    # do_test(2, [4, 5, 3, 2, 3, 9, 5, 7, 10, 4], [4, 4, 0, 4, 1, 2, 4, 0, 4, 0], 47, -1)
    # do_test(3, [3, 2, 5, 8, 8], [1, 3, 2, 1, 0], 20, 3)
    do_test(4, [6, 5, 2, 8, 8, 1, 6, 4], [1, 2, 1, 0, 1, 0, 3, 1], 23, 6)


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

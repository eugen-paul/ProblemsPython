from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        b = 2**17
        m = 2**17-1
        for n in nums:
            tmp = (n & m) - 1
            if nums[tmp] & b:
                return tmp+1
            nums[tmp] |= b

    def findDuplicate_1(self, nums: List[int]) -> int:
        cp = [False] * (len(nums)+1)
        for n in nums:
            if cp[n]:
                return n
            cp[n] = True


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findDuplicate(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 4, 2, 2], 2)
    do_test(1, [3, 1, 3, 4, 2], 3)
    do_test(2, [3, 3, 3, 3, 3], 3)


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

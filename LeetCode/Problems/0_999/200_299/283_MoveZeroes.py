from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last = 0
        for n in nums:
            if n != 0:
                nums[last] = n
                last += 1
        for i in range(last, len(nums)):
            nums[i] = 0

    def moveZeroes_1(self, nums: List[int]) -> None:
        cnt = nums.count(0)
        tmp = [n for n in nums if n != 0] + [0]*cnt
        nums.clear()
        nums.extend(tmp)


def do_test(i: int, s, r):
    c = Solution()
    resp = s[:]
    c.moveZeroes(resp)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
    do_test(1, [0], [0])
    do_test(2, [1, 2], [1, 2])


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

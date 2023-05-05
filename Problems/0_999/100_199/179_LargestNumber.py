from collections import defaultdict
from functools import cache, cmp_to_key
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber_i(self, nums):
        """sample solution"""
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

    def largestNumber(self, nums: List[int]) -> str:
        s = [str(n) for n in nums]

        def srt(a: str, b: str) -> int:
            ab = a+b
            ba = b+a
            for k, l in zip(ab, ba):
                if k > l:
                    return 1
                if k < l:
                    return -1
            return 0

        s.sort(reverse=True, key=cmp_to_key(srt))

        resp = "".join(s)
        i = 0
        while i < len(resp) and resp[i] == "0":
            i += 1
        if i == len(resp):
            return "0"
        return resp[i:]


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


def do_test(i: int, s, r):
    c = Solution()
    resp = c.largestNumber(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [10, 2], "210")
    do_test(1, [3, 30, 34, 5, 9], "9534330")
    do_test(2, [300, 301], "301300")
    do_test(3, [310, 301], "310301")
    do_test(4, [30, 301], "30301")
    do_test(5, [30, 331], "33130")
    do_test(6, [432, 43243], "43243432")
    do_test(7, [432, 43143], "43243143")
    do_test(8, [432, 43253], "43253432")
    do_test(9, [432, 43233], "43243233")
    do_test(10, [432, 43242], "43243242")
    do_test(11, [432, 43244], "43244432")
    do_test(12, [111311, 1113], "1113111311")
    do_test(13, [0, 0], "0")

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)

        max_len = nums[0].bit_length()

        f = [x for x in nums if x.bit_length() == max_len]
        resp = 0
        for n in nums[len(f):]:
            resp = resp | n

        cnt = Counter()
        for n in f:
            s = bin(n)
            for i, c in enumerate(s):
                if c == "1":
                    cnt[i-2] += 1

        best = 0
        for i, n in enumerate(f):
            s = bin(n)
            tmpCnt = Counter()
            for i, c in enumerate(s):
                if c == "1":
                    tmpCnt[i-2] += 1

            cnt = cnt-tmpCnt

            tr = n*(2**k)

            for j, o in cnt.items():
                if o == 0:
                    continue
                tr = tr | 2**(len(s)-j-3)

            cnt = cnt+tmpCnt
            best = max(best, resp | tr)

        return best


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maximumOr(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [12, 9], 1, 30)
    do_test(1, [8, 1, 2], 2, 35)


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

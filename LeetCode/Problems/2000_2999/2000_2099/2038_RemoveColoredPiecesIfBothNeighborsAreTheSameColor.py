from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) <= 2:
            return False
        cnt_a = 0
        cnt_b = 0
        last = "  "
        for i, c in enumerate(colors):
            if last == "AA" and c == "A":
                cnt_a += 1
            if last == "BB" and c == "B":
                cnt_b += 1
            last = last[1] + c
        return cnt_a > cnt_b


def do_test(i: int, s, r):
    c = Solution()
    resp = c.winnerOfGame(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "AAABABB", True)
    do_test(1, "AA", False)
    do_test(2, "ABBBBBBBAAA", False)


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

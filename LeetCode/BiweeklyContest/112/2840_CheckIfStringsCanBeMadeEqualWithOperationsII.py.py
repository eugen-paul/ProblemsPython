from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1Ev = [v for i,v in enumerate(s1) if i % 2 == 0]
        s1Od = [v for i,v in enumerate(s1) if i % 2 == 1]
        
        s2Ev = [v for i,v in enumerate(s2) if i % 2 == 0]
        s2Od = [v for i,v in enumerate(s2) if i % 2 == 1]
        
        return Counter(s1Ev) == Counter(s2Ev) and Counter(s1Od) == Counter(s2Od)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.checkStrings(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "abcdba", "cabdab", True)
    do_test(1, "abe", "bea", False)


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

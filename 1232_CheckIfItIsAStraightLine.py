from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        try:
            tn = (x2-x1) / (y2-y1)
        except ZeroDivisionError:
            return all([y == y1 for _, y in coordinates])

        i = 2
        while i < len(coordinates):
            x2, y2 = coordinates[i]
            try:
                tn2 = (x2-x1) / (y2-y1)
            except ZeroDivisionError:
                return False
            if tn != tn2:
                return False
            i += 1

        return True


class Solution_s:
    """sample solution"""

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def get_delta_x(a, b) -> int:
            return a[0]-b[0]

        def get_delta_y(a, b) -> int:
            return a[1]-b[1]

        dx = get_delta_x(coordinates[0], coordinates[1])
        dy = get_delta_y(coordinates[0], coordinates[1])

        for i in range(2, len(coordinates)):
            if dx * get_delta_y(coordinates[0], coordinates[i]) != dy * get_delta_x(coordinates[0], coordinates[i]):
                return False
        return True


def do_test(i: int, s, r):
    c = Solution()
    resp = c.checkStraightLine(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True)
    do_test(1, [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False)
    do_test(2, [[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]], True)

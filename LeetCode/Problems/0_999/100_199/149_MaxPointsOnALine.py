from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        count: dict[Tuple[str, str, int], Set[Tuple[int, int]]] = defaultdict(set)
        checked = []

        def get_func(p1, p2) -> Tuple[str, str, int]:
            if p1[0] == p2[0]:
                return (inf, -inf, p2[0])

            if p1[1] == p2[1]:
                return ("0", str(p1[1]), -inf)

            if p1[0] > p2[0]:
                p1, p2 = p2, p1

            d_y = p2[1]-p1[1]
            d_x = p2[0]-p1[0]
            gcd = math.gcd(d_y, d_x)
            d_y = d_y // gcd
            d_x = d_x // gcd
            st = str(d_y) + "/" + str(d_x)

            n_o = p1[1]*d_x - p1[0]*d_y
            gcd = math.gcd(d_y, n_o)
            n_o = n_o // gcd
            n_y = d_y // gcd
            n = str(n_o) + "/" + str(n_y)

            return (st, n, -inf)

        for point in points:
            for c in checked:
                count[get_func(point, c)].add((c[0], c[1]))
            checked.append(point)

        resp = 0
        for _, v in count.items():
            resp = max(resp, len(v))
        return resp + 1

    def maxPoints(self, points: List[List[int]]) -> int:
        """Sample solution"""
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result

def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxPoints(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 1], [2, 2], [3, 3]], 3)
    do_test(1, [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4)
    do_test(2, [[-6, -1], [3, 1], [12, 3]], 3)
    do_test(3, [[1, 0], [0, 0]], 2)
    do_test(4, [[1, 0], [0, 0], [4, 0], [10, 0], [10, 1]], 4)

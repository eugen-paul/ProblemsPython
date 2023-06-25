from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        q = [(v, k) for k, v in enumerate(queries)]
        q.sort()

        m: Dict[int, int] = dict()
        resp = [0] * len(q)

        l, r = 0, 0
        for end_time, k in q:
            start_time = end_time - x
            for r_pos in range(r, len(logs)):
                s, t = logs[r_pos]
                if t > end_time:
                    break
                m[s] = m.get(s, 0)+1
                r += 1

            for l_pos in range(l, len(logs)):
                s, t = logs[l_pos]
                if t >= start_time:
                    break
                l += 1
                m[s] -= 1
                if m[s] == 0:
                    m.pop(s)

            resp[k] = n-len(m)

        return resp


def do_test(i: int, s, n, p, k, r):
    c = Solution()
    resp = c.countServers(s, n, p, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11], [1, 2])
    do_test(1, 3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4], [0, 1])
    do_test(2, 4, [[4, 3], [2, 16], [1, 21], [3, 22], [1, 13], [3, 10], [2, 1], [1, 12], [4, 13], [2, 18]], 8, [14, 28, 29], [1, 2, 2])
    do_test(3, 6, [[1, 21]], 10, [24, 35, 28, 26, 20, 25, 16, 31, 12], [5, 6, 5, 5, 6, 5, 6, 5, 6])


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

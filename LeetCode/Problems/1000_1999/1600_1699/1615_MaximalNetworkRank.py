from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        m = [[False] * n for _ in range(n)]
        c = [0]*n
        for f, t in roads:
            m[f][t] = True
            m[t][f] = True
            c[f] += 1
            c[t] += 1
        ans = 0
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                cnt = c[a] + c[b]
                ans = max(ans, cnt if not m[a][b] else cnt-1)
        return ans

    def maximalNetworkRank_2(self, n: int, roads: List[List[int]]) -> int:
        m: Dict[int, List[int]] = defaultdict(list)
        for f, t in roads:
            m[f].append(t)
            m[t].append(f)
        ans = 0
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                cnt = len(m[a]) + len(m[b])
                ans = max(ans, cnt if a not in m[b] else cnt-1)
        return ans

    def maximalNetworkRank_1(self, n: int, roads: List[List[int]]) -> int:
        m: Dict[int, Set[int]] = defaultdict(set)
        for f, t in roads:
            m[f].add(t)
            m[t].add(f)
        ans = 0
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                cnt = len(m[a]) + len(m[b])
                ans = max(ans, cnt if a not in m[b] else cnt-1)
        return ans


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maximalNetworkRank(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, [[0, 1], [0, 3], [1, 2], [1, 3]], 4)
    do_test(1, 5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]], 5)
    do_test(2, 8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]], 5)
    do_test(3, 2, [[1, 0]], 1)


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

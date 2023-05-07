from collections import defaultdict
from functools import cache, cmp_to_key
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class UnionFind_by_rank:
    parent: List[int]
    rank: List[int]

    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        root_x: int = self.find(x)
        root_y: int = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """using sample solution"""
        uf = UnionFind_by_rank(n)

        edgeList.sort(key=lambda x: x[2])
        q = [[i, v] for i, v in enumerate(queries)]
        q.sort(key=lambda x: x[1][2])

        resp = [False] * len(queries)

        k = 0
        for i, v in q:
            f, t, c = v
            while k < len(edgeList) and edgeList[k][2] < c:
                uf.union(edgeList[k][0], edgeList[k][1])
                k += 1
            resp[i] = uf.connected(f, t)

        return resp

    def distanceLimitedPathsExist_1(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind_by_rank(n)

        full = [(1, f, t, c, 0) for f, t, c in edgeList]
        i = 0
        for f, t, c in queries:
            full.append((0, f, t, c, i))
            i += 1

        def my_comp(a, b):
            if a[3] == b[3]:
                return a[0]-b[0]
            return a[3]-b[3]

        full.sort(key=cmp_to_key(my_comp))

        resp = [False] * len(queries)

        for d, f, t, _, i in full:
            if d == 1:
                uf.union(f, t)
            else:
                resp[i] = uf.connected(t, f)

        return resp

    def distanceLimitedPathsExist_1(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """too slow"""
        g: Dict[int, Dict[int, int]] = dict()

        for f, t, c in edgeList:
            if f in g:
                if t in g[f]:
                    g[f][t] = min(g[f][t], c)
                else:
                    g[f][t] = c
            else:
                g[f] = {t: c}
            f, t = t, f
            if f in g:
                if t in g[f]:
                    g[f][t] = min(g[f][t], c)
                else:
                    g[f][t] = c
            else:
                g[f] = {t: c}

        resp = []
        for f, t, c in queries:
            visited = [False] * n
            q = []
            q.append(f)
            found = False
            while q:
                nxt = q.pop()
                if visited[nxt]:
                    continue
                visited[nxt] = True
                if nxt == t:
                    found = True
                    break
                for nb, w in g.get(nxt, dict()).items():
                    if w < c:
                        q.append(nb)

            resp.append(found)

        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.distanceLimitedPathsExist(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, 3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]], [False, True])
    do_test(1, 5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]], [True, False])

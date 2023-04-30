from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class UnionFind_by_rank:
    root: List[int]
    rank: List[int]
    components: int

    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.components = size

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
            self.components -= 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def is_full_connected(self) -> bool:
        return self.components == 1

    def copy(self) -> 'UnionFind_by_rank':
        resp = UnionFind_by_rank(1)
        resp.root = list(self.root)
        resp.rank = list(self.rank)
        resp.components = self.components
        return resp


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind_by_rank(n)
        count = 0
        for d, f, t in edges:
            if d != 3:
                continue
            if uf.connected(f-1, t-1):
                count += 1
            else:
                uf.union(f-1, t-1)

        auf = uf.copy()
        for d, f, t in edges:
            if d != 1:
                continue
            if auf.connected(f-1, t-1):
                count += 1
            else:
                auf.union(f-1, t-1)

        for d, f, t in edges:
            if d != 2:
                continue
            if uf.connected(f-1, t-1):
                count += 1
            else:
                uf.union(f-1, t-1)

        if not uf.is_full_connected() or not auf.is_full_connected():
            return -1

        return count

    def maxNumEdgesToRemove_1(self, n: int, edges: List[List[int]]) -> int:
        a = [[f-1, t-1] for d, f, t in edges if (d == 1)]
        b = [[f-1, t-1] for d, f, t in edges if (d == 2)]
        g = [[f-1, t-1] for d, f, t in edges if (d == 3)]

        uf = UnionFind_by_rank(n)
        count = 0
        for f, t in g:
            if uf.connected(f, t):
                count += 1
            else:
                uf.union(f, t)

        auf = uf.copy()
        for f, t in a:
            if auf.connected(f, t):
                count += 1
            else:
                auf.union(f, t)

        for f, t in b:
            if uf.connected(f, t):
                count += 1
            else:
                uf.union(f, t)

        for t in range(1, n):
            if not auf.connected(0, t) or not uf.connected(0, t):
                return -1

        return count


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxNumEdgesToRemove(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]], 2)
    do_test(1, 4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]], 0)
    do_test(2, 4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]], -1)
    do_test(3, 4, [[3, 1, 2], [3, 3, 4], [1, 1, 3], [2, 2, 4]], 0)

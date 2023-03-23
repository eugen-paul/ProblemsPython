from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class UnionFind:
    parent: List[int]
    rank: List[int]

    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [-1] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x: int, y: int):
        xset: int = self.find(x)
        yset: int = self.find(y)
        if xset == yset:
            return
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1


class Solution_i:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n:
            return -1
        uf = UnionFind(n)
        areas = n
        for f, t in connections:
            if uf.find(f) != uf.find(t):
                areas -= 1
                uf.union_set(f, t)
        return areas-1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n:
            return -1

        m = defaultdict(set)
        for f, t in connections:
            m[f].add(t)
            m[t].add(f)

        areas = n - len(m)

        while m:
            areas += 1
            s = set(m.popitem()[1])
            while s:
                nxt = s.pop()
                if nxt in m:
                    s.update(m.pop(nxt))
        return areas - 1

    def makeConnected_2(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n:
            return -1

        m = defaultdict(set)
        for f, t in connections:
            m[f].add(t)
            m[t].add(f)

        areas = n - len(m)

        while m:
            areas += 1
            to_check = Deque()
            to_check.extend(m.popitem()[1])
            while to_check:
                nxt = to_check.pop()
                if nxt in m:
                    to_check.extend(m.pop(nxt))
        return areas - 1

    def makeConnected_1(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n:
            return -1

        connected = set()
        m = defaultdict(set)
        for f, t in connections:
            m[f].add(t)
            m[t].add(f)
            connected.add(f)
            connected.add(t)

        areas = n - len(connected)

        while connected:
            areas += 1
            to_check = Deque()
            to_check.append(connected.pop())
            while to_check:
                nxt = to_check.pop()
                connected.discard(nxt)
                if nxt in m:
                    to_check.extend(m.pop(nxt))
        return areas - 1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.makeConnected(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, [[0, 1], [0, 2], [1, 2]], 1)
    do_test(1, 6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 2)
    do_test(2, 6, [[0, 1], [0, 2], [0, 3], [1, 2]], -1)

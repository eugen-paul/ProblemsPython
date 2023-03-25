from collections import defaultdict
from functools import cache
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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        un = UnionFind_by_rank(n)

        for f, t in edges:
            un.union(f, t)

        c = Counter()
        for i in range(n):
            c[un.find(i)] += 1

        resp = 0
        items = 0
        for _, count in c.items():
            resp += items * count
            items += count

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.countPairs(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, [[0, 1], [0, 2], [1, 2]], 0)
    do_test(1, 7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]], 14)

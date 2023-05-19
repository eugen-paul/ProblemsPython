from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import sys
input = sys.stdin.readline


def i_array_int() -> List[int]:
    return list(map(int, input().split()))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split())) for _ in range(h)]


class UnionFind_by_rank:
    root: List[int]
    rank: List[int]
    components: int  # Number of distinct components in the graph.

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


for _ in range(int(input())):
    n = int(input())
    a = i_array_int()
    a = [x-1 for x in a]

    un = UnionFind_by_rank(n)
    for i in range(n):
        un.union(i, a[i])

    ma = un.components

    full_circle = 0

    seen = [False] * n
    for i in range(len(a)):
        if seen[i]:
            continue

        seen[i] = True

        l = 1
        nxt = a[i]
        while not seen[nxt]:
            l += 1
            seen[nxt] = True
            nxt = a[nxt]

        if l > 2 and nxt == i:
            full_circle += 1

    print(min(ma, full_circle+1), ma)

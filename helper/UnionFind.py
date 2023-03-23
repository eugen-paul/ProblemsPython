from typing import List


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

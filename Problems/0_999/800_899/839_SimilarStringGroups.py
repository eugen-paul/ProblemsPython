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
    def numSimilarGroups_i(self, strs: List[str]) -> int:
        """sample solution"""
        def is_similar(a: str, b: str) -> bool:
            d = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    d += 1
            return d <= 2

        n = len(strs)
        dsu: UnionFind_by_rank = UnionFind_by_rank(n)
        count = n
        for i in range(n):
            for j in range(i+1, n):
                if is_similar(strs[i], strs[j]) and dsu.find(i) != dsu.find(j):
                    count -= 1
                    dsu.union(i, j)

        return count

    def numSimilarGroups(self, strs: List[str]) -> int:
        count = 0

        def is_similar(a: str, b: str) -> bool:
            d = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    d += 1
                if d > 2:
                    return False
            return d <= 2

        while strs:
            count += 1
            group = [strs.pop()]
            i = 0
            while i < len(group):
                cur = group[i]
                tmp = []
                for w in strs:
                    if is_similar(cur, w):
                        group.append(w)
                    else:
                        tmp.append(w)
                strs = tmp
                i += 1

        return count

    def numSimilarGroups_1(self, strs: List[str]) -> int:
        rest = set(strs)
        count = 0

        def is_similar(a: str, b: str) -> bool:
            d = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    d += 1
            return d <= 2

        while rest:
            count += 1
            group = [rest.pop()]
            i = 0
            while i < len(group):
                cur = group[i]
                sim = set()
                for w in rest:
                    if is_similar(cur, w):
                        sim.add(w)
                group += [*sim]
                rest = rest-sim
                i += 1

        return count


def do_test(i: int, s, r):
    c = Solution()
    resp = c.numSimilarGroups(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["tars", "rats", "arts", "star"], 2)
    do_test(1, ["omv", "ovm"], 1)
    do_test(2, ["blw", "bwl", "wlb"], 1)
    do_test(3, ["ajdidocuyh", "djdyaohuic", "ddjyhuicoa", "djdhaoyuic", "ddjoiuycha",
            "ddhoiuycja", "ajdydocuih", "ddjiouycha", "ajdydohuic", "ddjyouicha"], 2)

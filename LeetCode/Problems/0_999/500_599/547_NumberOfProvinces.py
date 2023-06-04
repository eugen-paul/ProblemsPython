from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class UnionFind_by_rank:
    # Time Complexity:
    # Union-find Constructor: O(N)
    # Find:                   O(logN)
    # Union:                  O(logN)
    # Connected:              O(logN)

    root: List[int]
    rank: List[int]
    components: int  # Number of distinct components in the graph.

    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.components = size

    def find(self, x: int):
        """The find function finds the root node of a given vertex.

        Args:
            x (int): vertex

        Returns:
            int: root node of a given vertex
        """
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        """The union function unions two vertices and makes their root nodes the same.

        Args:
            x (int): vertex
            y (int): vertex
        """
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
        """check if two vertices are connected 

        Returns:
            bool: there is a path from x to y / from y to x
        """
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        un = UnionFind_by_rank(len(isConnected[0]))
        for i, p in enumerate(isConnected):
            for j, v in enumerate(p):
                if v == 1:
                    un.union(i, j)

        return un.components


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findCircleNum(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2)
    do_test(1, [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3)

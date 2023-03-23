from typing import List

"""disjoint set / union-find. 
The primary use of disjoint sets is to address the connectivity between the components of a network.
Source: https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3881/
"""


class UnionFind_by_rank:
    # Time Complexity:
    # Union-find Constructor: O(N)
    # Find:                   O(logN)
    # Union:                  O(logN)
    # Connected:              O(logN)

    parent: List[int]
    rank: List[int]

    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

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

    def connected(self, x: int, y: int) -> bool:
        """check if two vertices are connected 

        Returns:
            bool: there is a path from x to y / from y to x
        """
        return self.find(x) == self.find(y)


class UnionFind_QuickUnion:
    # Time Complexity:
    # Union-find Constructor: O(N)
    # Find:                   O(N) in the worst-case
    # Union:                  O(N) in the worst-case
    # Connected:              O(N)
    root: List[int]

    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    def find(self, x: int):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class UnionFind_QuickFind:
    # Time Complexity:
    # Union-find Constructor: O(N)
    # Find:                   O(1)
    # Union:                  O(N)
    # Connected:              O(1)
    root: List[int]

    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    def find(self, x: int):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

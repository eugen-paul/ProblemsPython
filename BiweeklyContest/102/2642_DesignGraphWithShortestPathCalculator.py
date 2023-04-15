from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.m: Dict[Tuple[int, int]] = defaultdict(set)
        self.n = n
        for f, t, c in edges:
            self.m[f].add((t, c))

    def addEdge(self, edge: List[int]) -> None:
        self.m[edge[0]].add((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        d = []
        heapq.heapify(d)
        heapq.heappush(d, (0, node1))

        visited = [False] * self.n

        while d:
            cost, node = heapq.heappop(d)
            if node == node2:
                return cost
            if visited[node]:
                continue
            if node not in self.m:
                continue
            visited[node] = True
            for nxt, c in self.m[node]:
                heapq.heappush(d, (cost + c, nxt))
        return -1


def do_test(i: int, s, n, k):
    g: Graph = None
    i = 0
    for c in s:
        if c == "Graph":
            g = Graph(n[i][0], n[i][1])
        elif c == "addEdge":
            g.addEdge(n[i][0])
        elif c == "shortestPath":
            p = g.shortestPath(n[i][0], n[i][1])
            if p != k[i]:
                print("error")
            else:
                print("OK")
        i += 1


if __name__ == "__main__":
    do_test(0, ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"],
            [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]],
            [None, 6, -1, None, 6])

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


def kahnAlgo(n: int, edges: List[List[int]]) -> List[int]:
    graph: Dict[int, Set[int]] = defaultdict(set)

    # the number of edges entering node x
    indegree: List[int] = [0] * n

    for t, f in edges:
        graph[f].add(t)
        indegree[t] += 1

    # node to check for BSF. put all leaf nodes to q (indegree[x] == 0)
    q: List[int] = [x for x, v in enumerate(indegree) if v == 0]

    order = []
    nodes_seen = 0
    while q:
        node = q.pop(0)
        nodes_seen += 1
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return order if nodes_seen == n else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return kahnAlgo(numCourses, prerequisites)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findOrder(s, n)
    if resp in r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, [[1, 0]], [[0, 1]])
    do_test(1, 4, [[1, 0], [2, 0], [3, 1], [3, 2]], [[0, 1, 2, 3], [0, 2, 1, 3]])

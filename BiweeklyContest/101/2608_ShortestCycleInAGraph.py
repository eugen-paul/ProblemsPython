from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        m = defaultdict(set)
        for f, t in edges:
            m[f].add(t)
            m[t].add(f)

        smallest = inf
        is_smallest = False
        for i in range(n):
            d = Deque()
            for nb in m[i]:
                d.append((nb, i, 1))

            sub_visited = {i: 0}
            while d:
                node, last, cost = d.popleft()
                if cost >= smallest:
                    break
                if node in sub_visited:
                    is_smallest = True
                    smallest = min(smallest, cost + sub_visited[node])
                    break
                sub_visited[node] = cost
                for nxt in m[node]:
                    if nxt == last:
                        continue
                    d.append((nxt, node, cost+1))

        if is_smallest:
            return smallest
        return -1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findShortestCycle(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]], 3)
    do_test(1, 4, [[0, 1], [0, 2]], -1)
    do_test(2, 7, [[0, 1], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]], 4)
    do_test(3, 7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3], [6, 3]], 3)
    do_test(4, 4, [[2, 1], [0, 2], [3, 0]], -1)

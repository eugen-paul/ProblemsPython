from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        m: Dict[int, Set[Tuple[int, float]]] = defaultdict(set)
        for ft, p in zip(edges, succProb):
            f, t = ft
            m[f].add((t, p))
            m[t].add((f, p))

        q = []
        heapq.heappush(q, (-1, start))
        SEEN = set()

        while q:
            prob, node = heapq.heappop(q)
            if node == end:
                return -prob
            if node in SEEN:
                continue
            SEEN.add(node)
            for nxt, pr in m[node]:
                heapq.heappush(q, (prob * pr, nxt))

        return 0


def do_test(i: int, s, n, k, l, p, r):
    c = Solution()
    resp = c.maxProbability(s, n, k, l, p)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2, 0.25000)
    do_test(1, 3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2, 0.30000)
    do_test(2, 3, [[0, 1]], [0.5], 0, 2, 0.00000)

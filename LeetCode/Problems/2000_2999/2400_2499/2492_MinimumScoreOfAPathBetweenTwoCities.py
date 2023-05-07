from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        m: Dict[int, Set[Tuple[int, int]]] = defaultdict(set)
        for f, t, c in roads:
            m[f].add((t, c))
            m[t].add((f, c))

        to_check = Deque()
        to_check.append(1)

        visited = [False] * (n+1)
        resp = inf

        while to_check:
            point = to_check.pop()
            if visited[point]:
                continue
            visited[point] = True
            for t, c in m[point]:
                resp = min(resp, c)
                to_check.append(t)

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minScore(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5)
    do_test(1, 4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2)

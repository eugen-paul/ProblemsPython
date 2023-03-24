from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = {(a, b) for a, b in connections}
        m = defaultdict(set)
        for f, t in connections:
            m[f].add(t)
            m[t].add(f)

        visited = [False] * n
        to_check = Deque()
        to_check.append(0)
        resp = 0
        while to_check:
            cur = to_check.pop()
            if visited[cur]:
                continue
            visited[cur] = True
            for nxt in m[cur]:
                if (nxt, cur) not in roads and not visited[nxt]:
                    resp += 1
                to_check.append(nxt)
        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minReorder(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]], 3)
    do_test(1, 5, [[1, 0], [1, 2], [3, 2], [3, 4]], 2)
    do_test(2, 3, [[1, 0], [2, 0]], 0)

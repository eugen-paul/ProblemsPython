from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        g = [0] * len(graph)

        ok = True
        for i in range(len(graph)):
            if g[i] != 0:
                nb_collor = g[i] * (-1)
                for nb in graph[i]:
                    if g[nb] != nb_collor:
                        ok = False
            else:
                my_collor = 1
                q = []
                q.append((i, my_collor * (-1)))

                while q:
                    node, color = q.pop()
                    if g[node] != 0 and g[node] != color:
                        ok = False
                        break
                    if g[node] != 0:
                        continue
                    g[node] = color
                    for nb in graph[node]:
                        q.append((nb, color * -1))

            if not ok:
                break

        return ok


def do_test(i: int, s, r):
    c = Solution()
    resp = c.isBipartite(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False)
    do_test(1, [[1, 3], [0, 2], [1, 3], [0, 2]], True)

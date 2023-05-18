from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        targets = set()
        for _, t in edges:
            targets.add(t)

        return [i for i in range(n) if i not in targets]
    
    def findSmallestSetOfVertices_3(self, n: int, edges: List[List[int]]) -> List[int]:
        c = Counter()
        for _, t in edges:
            c[t] += 1

        return [i for i in range(n) if i not in c]
    

    def findSmallestSetOfVertices_2(self, n: int, edges: List[List[int]]) -> List[int]:
        m = defaultdict(set)
        for f, t in edges:
            m[f].add(t)

        resp = set()

        seen = [False] * n

        for i in range(n):
            if seen[i]:
                continue
            resp.add(i)
            q = Deque()
            q.append(i)
            while q:
                nxt = q.pop()
                for nn in m[nxt]:
                    if not seen[nn]:
                        q.append(nn)
                        seen[nn] = True
                    if nn in resp:
                        resp.remove(nn)

        return list(resp)

    def findSmallestSetOfVertices_1(self, n: int, edges: List[List[int]]) -> List[int]:
        m = defaultdict(set)
        for f, t in edges:
            m[f].add(t)

        resp = set()

        seen = [False] * n

        for i in range(n):
            if seen[i]:
                continue
            resp.add(i)
            q = [i]
            while q:
                nxt = q.pop()
                if seen[nxt]:
                    if nxt in resp:
                        resp.remove(nxt)
                    continue
                seen[nxt] = True
                for nn in m[nxt]:
                    q.append(nn)

        return list(resp)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findSmallestSetOfVertices(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]], [0, 3])
    do_test(1, 5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]], [0, 2, 3])

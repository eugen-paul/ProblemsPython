from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        m = defaultdict(set)
        for i in range(len(equations)):
            m[equations[i][0]].add((equations[i][1], values[i]))
            m[equations[i][1]].add((equations[i][0], 1 / values[i]))

        resp = []

        for a, b in queries:
            seen = set()
            q = []
            for nb in m[a]:
                q.append(nb)
                seen.add(nb[0])

            ok = False
            while q:
                nxt, val = q.pop()
                if nxt == b:
                    ok = True
                    resp.append(val)
                    break

                for nb in m[nxt]:
                    if nb[0] in seen:
                        continue
                    q.append((nb[0], nb[1] * val))
                    seen.add(nb[0])
            if not ok:
                resp.append(-1)

        return resp

    def calcEquation_1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        e = dict()
        m = defaultdict(set)
        for i in range(len(equations)):
            e[(equations[i][0], equations[i][1])] = values[i]
            e[(equations[i][1], equations[i][0])] = 1 / values[i]

            m[equations[i][0]].add((equations[i][0], equations[i][1]))
            m[equations[i][1]].add((equations[i][1], equations[i][0]))

        resp = []

        for a, b in queries:
            if (a, b) in e:
                resp.append(e[(a, b)])
                continue
            if a not in m or b not in m:
                resp.append(-1)
                continue

            seen = set()
            q = []
            for k in m[a]:
                q.append((k, e[k]))
                seen.add(k)

            ok = False
            while q:
                nxt, val = q.pop()
                if nxt[1] == b:
                    ok = True
                    resp.append(val)
                    break

                for k in m[nxt[1]]:
                    if k in seen:
                        continue
                    q.append((k, e[k] * val))
                    seen.add(k)
            if not ok:
                resp.append(-1)

        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.calcEquation(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0,
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
            )
    do_test(1,
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            [3.75000, 0.40000, 5.00000, 0.20000]
            )
    do_test(2,
            [["a", "b"]],
            [0.5],
            [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
            [0.50000, 2.00000, -1.00000, -1.00000]
            )

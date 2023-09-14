from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

from sortedcontainers import SortedList

# import sys
# sys.setrecursionlimit(10000)


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        m: Dict[str, List[str]] = defaultdict(list)
        for f, t in tickets:
            m[f].append(t)
        for v in m.values():
            v.sort()

        def solve(start: str, m: Dict[str, List[str]]) -> List[str]:
            if len(m) == 0:
                return []
            if start not in m:
                return None

            targets = m[start][:]
            if len(targets) == 1:
                del m[start]
                tmp = solve(targets[0], m)
                m[start] = targets
                if tmp is not None:
                    return [targets[0]] + tmp
                return None

            for i, t in enumerate(targets):
                m[start] = targets[:i] + targets[i+1:]
                tmp = solve(t, m)
                if tmp is not None:
                    return [t] + tmp
                m[start] = targets

            return None

        way = solve("JFK", m)
        return ["JFK"]+way

    def findItinerary_1(self, tickets: List[List[str]]) -> List[str]:
        m: Dict[List[List]] = defaultdict(SortedList)

        for d, f in tickets:
            m[d].add([f, False])

        def way(start: str, m: Dict[str, List[str]], cnt: int) -> List[str]:
            if cnt == len(tickets):
                return [start]

            if start not in m:
                return None

            for target in m[start]:
                if target[1]:
                    continue

                target[1] = True
                resp = way(target[0], m, cnt + 1)
                target[1] = False

                if resp != None:
                    return [start] + resp
            return None

        return way("JFK", m, 0)

    def findItinerary_i(self, tickets: List[List[str]]) -> List[str]:
        """internet solution:
        https://leetcode.com/problems/reconstruct-itinerary/solutions/3541609/9-lines-dfs/"""
        def dfs(city):
            while len(g[city]):
                dfs(g[city].pop(0))
            res.insert(0, city)

        res, g = [], defaultdict(list)
        for u, v in sorted(tickets):
            g[u].append(v)

        dfs('JFK')
        return res

    def findItinerary_1(self, tickets: List[List[str]]) -> List[str]:
        m: Dict[List[str]] = defaultdict(SortedList)

        for d, f in tickets:
            m[d].add(f)

        def way(start: str, m: Dict[str, List[str]]) -> List[str]:
            if len(m) == 0:
                return [start]

            if start not in m:
                return None

            for i in range(len(m[start])):
                target = m[start][i]
                m[start].pop(i)
                if len(m[start]) == 0:
                    del m[start]
                resp = way(target, m)
                m[start].add(target)
                if resp != None:
                    return [start] + resp
            return None

        return way("JFK", m)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findItinerary(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0,
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            ["JFK", "MUC", "LHR", "SFO", "SJC"]
            )
    do_test(1,
            [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
            )
    do_test(2,
            [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
            ["JFK", "NRT", "JFK", "KUL"]
            )

from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution_i:
    """internet solution:
    https://leetcode.com/problems/time-needed-to-inform-all-employees/solutions/3591009/python-java-c-simple-solution-easy-to-understand/
    """

    def dfs(self, manager, informTime, adjList):
        maxTime = 0
        for subordinate in adjList[manager]:
            maxTime = max(maxTime, self.dfs(subordinate, informTime, adjList))
        return maxTime + informTime[manager]

    def numOfMinutes(self, n, headID, manager, informTime):
        adjList = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                adjList[manager[i]].append(i)

        return self.dfs(headID, informTime, adjList)


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        m = defaultdict(set)
        for i, e in enumerate(manager):
            m[e].add(i)

        q = []
        heapq.heapify(q)
        heapq.heappush(q, (0, headID))

        resp = 0

        while q:
            t, emp = heapq.heappop(q)
            for nxt in m[emp]:
                heapq.heappush(q, (t+informTime[emp], nxt))
            resp = t

        return resp


def do_test(i: int, s, n, k, l, r):
    c = Solution()
    resp = c.numOfMinutes(s, n, k, l)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 1, 0, [-1], [0], 0)
    do_test(1, 6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0], 1)

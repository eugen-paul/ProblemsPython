import bisect
from collections import defaultdict
from functools import cache, lru_cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        to_check = Deque()
        to_check.append((0, 0))

        d = [0] * 396
        k = 0
        for i in range(396):
            if k < len(days) and days[k] == i:
                k += 1
            d[i] = k

        visited = [inf] * 365

        best = inf
        while to_check:
            f, cost = to_check.popleft()
            if cost >= best:
                continue
            if f >= len(days):
                best = cost
                continue
            if visited[f] <= cost:
                continue
            visited[f] = cost

            to_check.append((f+1, cost + costs[0]))

            to_check.append((d[days[f]+6], cost + costs[1]))
            to_check.append((d[days[f]+29], cost + costs[2]))

        return best

    def mincostTickets_i(self, days, costs):
        """sample solution"""
        dayset = set(days)
        durations = [1, 7, 30]

        # dp(i)=min(
        #           dp(i+1) +costs[0],
        #           dp(i+7) +costs[1],
        #           dp(i+30)+costs[2]
        #          )
        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)

    def mincostTickets_1(self, days: List[int], costs: List[int]) -> int:
        to_check = Deque()
        to_check.append((0, 0))

        visited = [inf] * 365

        best = inf
        while to_check:
            f, cost = to_check.popleft()
            if cost >= best:
                continue
            if f >= len(days):
                best = cost
                continue
            if visited[f] <= cost:
                continue
            visited[f] = cost

            to_check.append((f+1, cost + costs[0]))

            to_check.append((bisect.bisect_left(days, days[f]+7), cost + costs[1]))
            to_check.append((bisect.bisect_left(days, days[f]+30), cost + costs[2]))

        return best


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.mincostTickets(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 4, 6, 7, 8, 20], [2, 7, 15], 11)
    do_test(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17)
    do_test(2, [1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28], [3, 13, 45], 44)

import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        dp = [[inf] * (len(cuts)) for _ in range(len(cuts))]
        for i in range(len(cuts)):
            dp[1][i] = 0

        for ln in range(2, len(cuts)):
            for start in range(len(cuts)-ln):
                for cl in range(1, ln):
                    dp[ln][start] = min(
                        dp[ln][start],
                        cuts[start+ln] - cuts[start] + dp[cl][start] + dp[ln-cl][start+cl]
                    )

        return dp[-1][0]

    def minCost_1(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        @cache
        def cost(mi, ma) -> int:
            pos_mi = bisect.bisect_left(cuts, mi)
            pos_ma = bisect.bisect_left(cuts, ma)
            if pos_mi+1 == pos_ma:
                return 0

            resp = inf
            for p in range(pos_mi+1, pos_ma):
                resp = min(resp, cost(mi, cuts[p]) + cost(cuts[p], ma) + ma - mi)
            return resp

        return cost(0, n)

    def minCost_f(self, n: int, cuts: List[int]) -> int:
        """wrong"""
        cuts.sort()
        cuts = [0] + cuts + [n]

        def cost(mi, ma) -> int:
            pos_mi = bisect.bisect_left(cuts, mi)
            pos_ma = bisect.bisect_left(cuts, ma)
            if pos_mi+1 == pos_ma:
                return 0

            mit = (ma + mi) // 2
            pos_mit = bisect.bisect_left(cuts, mit)
            if pos_mit == len(cuts):
                return 0
            if pos_mit == pos_ma:
                pos_mit -= 1

            resp = cost(mi, cuts[pos_mit]) + cost(cuts[pos_mit], ma) + ma - mi
            if pos_mit - 1 > pos_mi:
                resp = min(resp, cost(mi, cuts[pos_mit-1]) + cost(cuts[pos_mit-1], ma) + ma - mi)
            if pos_mit + 1 < pos_ma:
                resp = min(resp, cost(mi, cuts[pos_mit+1]) + cost(cuts[pos_mit+1], ma) + ma - mi)

            return resp

        return cost(0, n)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minCost(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 7, [1, 3, 4, 5], 16)
    do_test(1, 9, [5, 6, 1, 4, 2], 22)
    do_test(2, 10, [7, 8, 9, 2, 1], 24)

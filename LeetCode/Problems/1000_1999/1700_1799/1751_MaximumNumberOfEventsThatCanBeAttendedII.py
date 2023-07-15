import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

import sys
sys.setrecursionlimit(1000000)


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        m = dict()

        def solve(pos: int, rest: int) -> int:
            if pos == len(events) or rest == 0:
                return 0
            rest = min(rest, len(events) - pos)
            if (pos, rest) in m:
                return m[(pos, rest)]

            resp = events[pos][2]
            pp = pos+1
            while pp < len(events) and events[pp][0] <= events[pos][1]:
                pp+=1
            if pp < len(events):
                resp = max(resp + solve(pp, rest-1), solve(pos+1,rest))
            else:
                resp = max(resp, solve(pos+1,rest))

            m[(pos, rest)] = resp
            return resp

        return solve(0, k)
    
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        ends = [(e[0], i) for i, e in enumerate(events)]
        ends.sort()
        
        m = dict()

        def solve(pos: int, rest: int) -> int:
            if pos == len(events) or rest == 0:
                return 0
            rest = min(rest, len(events) - pos)
            if (pos, rest) in m:
                return m[(pos, rest)]

            resp = events[pos][2]
            pp = bisect.bisect_right(ends, (events[pos][1], inf))
            if pp < len(events):
                resp = max(resp + solve(pp, rest-1), solve(pos+1,rest))
            else:
                resp = max(resp, solve(pos+1,rest))

            m[(pos, rest)] = resp
            return resp

        return solve(0, k)

    def maxValue_s(self, events: List[List[int]], k: int) -> int:        
        """sample solution"""
        n = len(events)
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        events.sort()
        starts = [start for start, _, _ in events]

        for cur_index in range(n - 1, -1, -1):
            for count in range(1, k + 1):
                next_index = bisect.bisect_right(starts, events[cur_index][1])
                dp[count][cur_index] = max(dp[count][cur_index + 1], events[cur_index][2] + dp[count - 1][next_index])
        
        return dp[k][0]

def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxValue(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2, 7)
    do_test(1, [[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2, 10)
    do_test(2, [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3, 9)
    do_test(3, [[41,57,75],[35,100,50],[52,66,10],[57,96,17],[66,99,40],[12,73,51],[42,65,94],[79,94,7],[22,64,84],[54,54,65],[61,64,49],[5,12,68],[57,89,25],[40,79,93],[42,92,17],[72,75,3],[73,90,34],[39,46,75],[2,6,18],[77,93,7],[36,46,73],[18,85,12],[23,43,71],[8,14,7],[78,91,55],[80,84,88],[9,77,64],[51,56,96],[4,6,85],[96,96,13],[9,82,26],[75,78,58],[7,41,53],[12,86,21],[82,83,63],[5,48,81],[19,91,14],[2,92,71],[83,93,66],[6,11,80],[42,94,65],[38,44,8],[21,29,61],[50,61,2]], 40, 532)

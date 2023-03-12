from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def check_way(start: int) -> int:
            tank = gas[start]
            w = 0
            for i in range(start+1, len(gas) + start + 1):
                k = i % len(gas)
                if tank < cost[k-1]:
                    return w
                tank = tank - cost[k-1] + gas[k]
                w += 1
            return w

        i = 0
        while True:
            if i >= len(gas):
                break
            w = 0
            if cost[i] <= gas[i]:
                w = check_way(i)
                if w == len(gas):
                    return i
            i += w + 1
        return -1

    def canCompleteCircuit_1(self, gas: List[int], cost: List[int]) -> int:
        visited = [-1] * len(gas)

        def check_way(start: int) -> bool:
            tank = gas[start]
            if visited[start] >= tank:
                return False
            visited[start] = 0

            for i in range(start+1, len(gas) + start + 1):
                k = i % len(gas)
                if tank < cost[k-1]:
                    return False
                tank = tank - cost[k-1] + gas[k]
                if visited[k] >= tank:
                    return False
                visited[k] = tank

            return True

        for i in range(len(gas)):
            if cost[i] > gas[i]:
                continue
            if check_way(i):
                return i
        return -1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.canCompleteCircuit(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3)
    do_test(1, [2, 3, 4], [3, 4, 3], -1)
    do_test(2, [5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4)

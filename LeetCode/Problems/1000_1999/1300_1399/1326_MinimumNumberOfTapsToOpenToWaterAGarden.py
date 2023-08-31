from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        pass

    def minTaps_s(self, n: int, ranges: List[int]) -> int:
        """sample solution"""
        # Define an infinite value
        INF = int(1e9)

        # Create a list to store the minimum number of taps needed for each position
        dp = [INF] * (n + 1)

        # Initialize the starting position of the garden
        dp[0] = 0

        for i in range(n + 1):
            # Calculate the leftmost position reachable by the current tap
            tap_start = max(0, i - ranges[i])
            # Calculate the rightmost position reachable by the current tap
            tap_end = min(n, i + ranges[i])

            for j in range(tap_start, tap_end + 1):
                # Update with the minimum number of taps
                dp[tap_end] = min(dp[tap_end], dp[j] + 1)

        # Check if the garden can be watered completely
        if dp[n] == INF:
            # Garden cannot be watered
            return -1

        # Return the minimum number of taps needed to water the entire garden
        return dp[n]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minTaps(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 5, [3, 4, 1, 1, 0, 0], 1)
    do_test(1, 3, [0, 0, 0, 0], -1)
    do_test(2, 3, [0, 0, 0, 1], -1)
    do_test(3, 3, [0, 2, 0, 0], 1)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

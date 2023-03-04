from collections import defaultdict
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()

        groups_count = 1
        end = ranges[0][1]

        for g in ranges:
            if end < g[0]:
                groups_count += 1
                end = g[1]
            else:
                end = max(g[1],end)

        return pow(2, groups_count, 1000000000 + 7)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.countWays(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[6, 10], [5, 15]], 2)
    do_test(1, [[1, 3], [10, 20], [2, 5], [4, 8]], 4)
    do_test(2, [[0, 2], [2, 3]], 2)
    do_test(3, [[34, 56], [28, 29], [12, 16], [11, 48], [28, 54], [22, 55], [28, 41], [41, 44]], 2)

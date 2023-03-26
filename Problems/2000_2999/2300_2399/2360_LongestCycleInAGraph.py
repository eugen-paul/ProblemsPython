from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        m = {k: v for k, v in enumerate(edges)}

        start_from = [-1] * len(m)

        resp = -1
        for start in range(len(m)):
            if start_from[start] != -1:
                continue
            cur = start
            while cur != -1 and start_from[cur] == -1:
                start_from[cur] = start
                cur = m.get(cur, -1)
            if cur != -1 and start_from[cur] == start:
                count = 1
                nxt = m.get(cur)
                while nxt != cur:
                    nxt = m.get(nxt)
                    count += 1
                resp = max(resp, count)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestCycle(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 3, 4, 2, 3], 3)
    do_test(1, [2, -1, 3, 1], -1)
    do_test(2, [-1, 2, -1, -1], -1)

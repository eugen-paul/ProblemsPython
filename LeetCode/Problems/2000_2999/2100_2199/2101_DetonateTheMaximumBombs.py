from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        m = defaultdict(list)

        def in_range(a, b) -> bool:
            x1, y1, r1 = a
            x2, y2, _ = b
            return abs(x1-x2) ** 2 + abs(y1-y2) ** 2 <= r1 ** 2

        for i, b1 in enumerate(bombs):
            for j in range(i+1, len(bombs)):
                b2 = bombs[j]
                if in_range(b1, b2):
                    m[i].append(j)
                if in_range(b2, b1):
                    m[j].append(i)

        resp = 0
        for i in range(len(bombs)):
            q = [i]

            tmp = 1
            SEEN = set()
            SEEN.add(i)

            while q:
                cur = q.pop()
                for nxt in m[cur]:
                    if nxt not in SEEN:
                        SEEN.add(nxt)
                        q.append(nxt)
                        tmp += 1
            resp = max(tmp, resp)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maximumDetonation(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[2, 1, 3], [6, 1, 4]], 2)
    do_test(1, [[1, 1, 5], [10, 10, 5]], 1)
    do_test(2, [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], 5)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

import sys
sys.setrecursionlimit(1000000)


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """sample solution"""

        # We collect and sort the value of all n - 1 pairs.
        n = len(weights)
        pair_weights = [0] * (n - 1)
        for i in range(n - 1):
            pair_weights[i] = weights[i] + weights[i + 1]
        pair_weights.sort()

        # Get the difference between the largest k - 1 values and the
        # smallest k - 1 values.
        answer = 0
        for i in range(k - 1):
            answer += pair_weights[n - 2 - i] - pair_weights[i]

        return answer

    def putMarbles_1(self, weights: List[int], k: int) -> int:
        """too slow"""
        n = len(weights)

        m = dict()

        def solve(pos: int, k: int) -> Tuple[int, int]:
            if k == 1:
                return (weights[pos] + weights[-1], weights[pos] + weights[-1])
            if (pos, k) in m:
                return m[(pos, k)]
            resp = (inf, -inf)
            start = weights[pos]
            for i in range(pos, n-k+1):
                cur_score = weights[i] + start
                r = solve(i+1, k-1)
                resp = (
                    min(resp[0], cur_score + r[0]),
                    max(resp[1], cur_score + r[1])
                )
            m[(pos, k)] = resp
            return resp

        resp = solve(0, k)
        return resp[1]-resp[0]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.putMarbles(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 5, 1], 2, 4)
    do_test(1, [1, 3], 2, 0)
    do_test(2, [1, 4, 2, 5, 2], 3, 3)

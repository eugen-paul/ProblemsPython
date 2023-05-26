from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def stoneGameII_s(self, piles: List[int]) -> int:
        """sample solution"""
        n = len(piles)
        dp = [[[-1] * (n + 1) for i in range(n + 1)] for p in range(0, 2)]

        def f(p, i, m):
            if i == n:
                return 0
            if dp[p][i][m] != -1:
                return dp[p][i][m]
            res = 1000000 if p == 1 else -1
            s = 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if p == 0:
                    res = max(res, s + f(1, i + x, max(m, x)))
                else:
                    res = min(res, f(0, i + x, max(m, x)))
            dp[p][i][m] = res
            return res

        return f(0, 0, 1)

    def stoneGameII(self, piles: List[int]) -> int:

        r = piles[:] + [0]
        for i in range(len(piles)-1, -1, -1):
            r[i] += r[i+1]

        mem = [[-1] * (len(piles)+1) for _ in range(len(piles)+1)]

        def do(m: int, pos: int) -> int:
            if len(piles) <= pos:
                return 0
            if mem[m][pos] != -1:
                return mem[m][pos]

            resp = 0
            tmp_a = 0
            for am in range(1, min(m*2 + 1, len(piles)-pos+1)):
                end_a = min(pos + am, len(piles))
                tmp_a += piles[end_a-1]
                enemy_rest = do(max(am, m), end_a)
                resp = max(tmp_a + r[end_a] - enemy_rest, resp)
            mem[m][pos] = resp
            return resp

        return do(1, 0)

    def stoneGameII_2(self, piles: List[int]) -> int:

        r = piles[:] + [0]
        for i in range(len(piles)-1, -1, -1):
            r[i] += r[i+1]

        @cache
        def do(m: int, pos: int) -> int:
            if len(piles) <= pos:
                return 0

            resp = 0
            tmp_a = 0
            for am in range(1, min(m*2 + 1, len(piles)-pos+1)):
                end_a = min(pos + am, len(piles))
                tmp_a += piles[end_a-1]
                enemy_rest = do(max(am, m), end_a)
                resp = max(tmp_a + r[end_a] - enemy_rest, resp)
            return resp

        return do(1, 0)

    def stoneGameII_1(self, piles: List[int]) -> int:

        @cache
        def do(m: int, pos: int) -> int:
            if len(piles) <= pos:
                return 0

            resp = 0
            # Alice turn
            for am in range(1, min(m*2 + 1, len(piles)-pos+1)):
                end_a = min(pos + am, len(piles))
                tmp_a = sum(piles[pos:end_a])

                bob_m = max(am, m)
                bobs_best = inf
                # Bob turn
                for ab in range(1, min(bob_m*2 + 1, len(piles)-pos+1)):
                    end_b = min(end_a + ab, len(piles))
                    # tmp_b = sum(piles[end_a:end_b])
                    alice_rest = do(max(ab, bob_m), end_b)
                    if bobs_best > alice_rest:
                        bobs_best = alice_rest
                resp = max(bobs_best+tmp_a, resp)
            return resp

        return do(1, 0)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.stoneGameII(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 7, 9, 4, 4], 10)
    do_test(1, [1, 2, 3, 4, 5, 100], 104)
    do_test(2, [1], 1)
    do_test(3, [795, 6723, 7450, 2744, 5780, 4465, 1910, 4079, 5624, 9127, 1147, 5613, 1428, 9187, 9177, 9161, 3498, 6182, 9720, 4584, 7317, 7829, 464, 6273, 6440, 6132, 743, 162, 5025, 9862, 5686, 441, 8984, 1219, 1815, 7082, 5510, 3587, 4039, 7520, 7889, 5078, 5248, 6428, 9705, 2252,
            1412, 5397, 9240, 5428, 7593, 3252, 3513, 9428, 2938, 7096, 1431, 1933, 4725, 7574, 6802, 3179, 8558, 8642, 9637, 5112, 7667, 2753, 7258, 5737, 1021, 429, 1367, 6181, 1605, 202, 6873, 7285, 4521, 9737, 6160, 5196, 1885, 7443, 9445, 2401, 4689, 3280, 2293, 2261, 8183], 234604)

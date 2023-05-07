from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def ways_s(self, pizza: List[str], k: int) -> int:
        """Sample solution"""
        rows = len(pizza)
        cols = len(pizza[0])
        apples = [[0] * (cols + 1) for row in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                apples[row][col] = ((pizza[row][col] == 'A')
                                    + apples[row + 1][col]
                                    + apples[row][col + 1]
                                    - apples[row + 1][col + 1])
        dp = [[[0 for col in range(cols)] for row in range(rows)] for remain in range(k)]
        dp[0] = [[int(apples[row][col] > 0) for col in range(cols)] for row in range(rows)]
        mod = 1000000007
        for remain in range(1, k):
            for row in range(rows):
                for col in range(cols):
                    val = 0
                    for next_row in range(row + 1, rows):
                        if apples[row][col] - apples[next_row][col] > 0:
                            val += dp[remain - 1][next_row][col]
                    for next_col in range(col + 1, cols):
                        if apples[row][col] - apples[row][next_col] > 0:
                            val += dp[remain - 1][row][next_col]
                    dp[remain][row][col] = val % mod
        return dp[k - 1][0][0]

    def ways(self, pizza: List[str], k: int) -> int:
        @cache
        def count_apple(start_x: int, start_y: int, end_x: int, end_y) -> int:
            resp = 0
            for x in range(start_x, end_x):
                for y in range(start_y, end_y):
                    if pizza[y][x] == 'A':
                        resp += 1
            return resp

        @cache
        def sub_h(start_x: int, start_y: int, person: int) -> int:
            if start_x >= len(pizza[0]) or start_y >= len(pizza):
                return 0
            if count_apple(start_x, start_y, len(pizza[0]), len(pizza)) < person:
                return 0
            if person == 1:
                return 1

            resp = 0
            count_ok = False
            for i in range(start_x, len(pizza[0]) - 1):
                if not count_ok:
                    count_left = count_apple(start_x, start_y, i + 1, len(pizza))
                    count_ok = (count_left > 0)
                if count_left > 0:
                    resp += sub_v(i + 1, start_y, person - 1)

            return resp % 1000000007

        @cache
        def sub_v(start_x: int, start_y: int, person: int) -> int:
            if start_x >= len(pizza[0]) or start_y >= len(pizza):
                return 0
            if count_apple(start_x, start_y, len(pizza[0]), len(pizza)) < person:
                return 0
            if person == 1:
                return 1

            resp = 0
            count_ok = False
            for i in range(start_y, len(pizza)):
                if not count_ok:
                    count_upper = count_apple(start_x, start_y, len(pizza[0]), i)
                    count_ok = (count_upper > 0)
                if i == start_y:
                    resp += sub_h(start_x, start_y, person)
                elif count_upper > 0:
                    resp += sub_v(start_x, i, person - 1)

            return resp % 1000000007

        return sub_v(0, 0, k)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.ways(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        "A..",
        "AAA",
        "..."
    ],
        3, 3)
    do_test(1, [
        "A..",
        "AA.",
        "..."
    ],
        3, 1)
    do_test(2, [
        "A..",
        "A..",
        "..."
    ],
        1, 1)
    do_test(3, [
        "A",
        "A",
        "A"
    ],
        3, 1)
    do_test(4, [
        "AAA"
    ],
        3, 1)
    do_test(5, [
        "..A.A.AAA...AAAAAA.AA..A..A.A......A.AAA.AAAAAA.AA",
        "A.AA.A.....AA..AA.AA.A....AAA.A........AAAAA.A.AA.",
        "A..AA.AAA..AAAAAAAA..AA...A..A...A..AAA...AAAA..AA",
        "....A.A.AA.AA.AA...A.AA.AAA...A....AA.......A..AA.",
        "AAA....AA.A.A.AAA...A..A....A..AAAA...A.A.A.AAAA..",
        "....AA..A.AA..A.A...A.A..AAAA..AAAA.A.AA..AAA...AA",
        "A..A.AA.AA.A.A.AA..A.A..A.A.AAA....AAAAA.A.AA..A.A",
        ".AA.A...AAAAA.A..A....A...A.AAAA.AA..A.AA.AAAA.AA.",
        "A.AA.AAAA.....AA..AAA..AAAAAAA...AA.A..A.AAAAA.A..",
        "A.A...A.A...A..A...A.AAAA.A..A....A..AA.AAA.AA.AA.",
        ".A.A.A....AAA..AAA...A.AA..AAAAAAA.....AA....A....",
        "..AAAAAA..A..A...AA.A..A.AA......A.AA....A.A.AAAA.",
        "...A.AA.AAA.AA....A..AAAA...A..AAA.AAAA.A.....AA.A",
        "A.AAAAA..A...AAAAAAAA.AAA.....A.AAA.AA.A..A.A.A...",
        "A.A.AA...A.A.AA...A.AA.AA....AA...AA.A..A.AA....AA",
        "AA.A..A.AA..AAAAA...A..AAAAA.AA..AA.AA.A..AAAAA..A",
        "...AA....AAAA.A...AA....AAAAA.A.AAAA.A.AA..AA..AAA",
        "..AAAA..AA..A.AA.A.A.AA...A...AAAAAAA..A.AAA..AA.A",
        "AA....AA....AA.A......AAA...A...A.AA.A.AA.A.A.AA.A",
        "A.AAAA..AA..A..AAA.AAA.A....AAA.....A..A.AA.A.A...",
        "..AA...AAAAA.A.A......AA...A..AAA.AA..A.A.A.AA..A.",
        ".......AA..AA.AAA.A....A...A.AA..A.A..AAAAAAA.AA.A",
        ".A.AAA.AA..A.A.A.A.A.AA...AAAA.A.A.AA..A...A.AAA..",
        "A..AAAAA.A..A..A.A..AA..A...AAA.AA.A.A.AAA..A.AA..",
        "A.AAA.A.AAAAA....AA..A.AAA.A..AA...AA..A.A.A.AA.AA",
        ".A..AAAA.A.A.A.A.......AAAA.AA...AA..AAA..A...A.AA",
        "A.A.A.A..A...AA..A.AAA..AAAAA.AA.A.A.A..AA.A.A....",
        "A..A..A.A.AA.A....A...A......A.AA.AAA..A.AA...AA..",
        ".....A..A...A.A...A..A.AA.A...AA..AAA...AA..A.AAA.",
        "A...AA..A..AA.A.A.AAA..AA..AAA...AAA..AAA.AAAAA...",
        "AA...AAA.AAA...AAAA..A...A..A...AA...A..AA.A...A..",
        "A.AA..AAAA.AA.AAA.A.AA.A..AAAAA.A...A.A...A.AA....",
        "A.......AA....AA..AAA.AAAAAAA.A.AA..A.A.AA....AA..",
        ".A.A...AA..AA...AA.AAAA.....A..A..A.AA.A.AA...A.AA",
        "..AA.AA.AA..A...AA.AA.AAAAAA.....A.AA..AA......A..",
        "AAA..AA...A....A....AA.AA.AA.A.A.A..AA.AA..AAA.AAA",
        "..AAA.AAA.A.AA.....AAA.A.AA.AAAAA..AA..AA.........",
        ".AA..A......A.A.AAA.AAAA...A.AAAA...AAA.AAAA.....A",
        "AAAAAAA.AA..A....AAAA.A..AA.A....AA.A...A.A....A..",
        ".A.A.AA..A.AA.....A.A...A.A..A...AAA..A..AA..A.AAA",
        "AAAA....A...A.AA..AAA..A.AAA..AA.........AA.AAA.A.",
        "......AAAA..A.AAA.A..AAA...AAAAA...A.AA..A.A.AA.A.",
        "AA......A.AAAAAAAA..A.AAA...A.A....A.AAA.AA.A.AAA.",
        ".A.A....A.AAA..A..AA........A.AAAA.AAA.AA....A..AA",
        ".AA.A...AA.AAA.A....A.A...A........A.AAA......A...",
        "..AAA....A.A...A.AA..AAA.AAAAA....AAAAA..AA.AAAA..",
        "..A.AAA.AA..A.AA.A...A.AA....AAA.A.....AAA...A...A",
        ".AA.AA...A....A.AA.A..A..AAA.A.A.AA.......A.A...A.",
        "...A...A.AA.A..AAAAA...AA..A.A..AAA.AA...AA...A.A.",
        "..AAA..A.A..A..A..AA..AA...A..AA.AAAAA.A....A..A.A"
    ],
        8, 641829390)

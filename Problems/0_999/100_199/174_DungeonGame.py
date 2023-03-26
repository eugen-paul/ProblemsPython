from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        df = [[None] * len(l) for l in dungeon]

        df[-1][-1] = dungeon[-1][-1]

        x = len(dungeon[0])-1
        for y in range(len(dungeon)-2, -1, -1):
            df[y][x] = min(df[y+1][x] + dungeon[y][x], dungeon[y][x], 0)

        y = len(dungeon)-1
        for x in range(len(dungeon[0])-2, -1, -1):
            df[y][x] = min(df[y][x+1] + dungeon[y][x], dungeon[y][x], 0)

        for y in range(len(dungeon)-2, -1, -1):
            for x in range(len(dungeon[0])-2, -1, -1):
                point_cost_d = min(df[y+1][x] + dungeon[y][x], dungeon[y][x], 0)
                min_life_d = max(
                    -dungeon[y][x] + 1 if dungeon[y][x] < 0 else 1,
                    -point_cost_d + 1 if point_cost_d < 0 else 1
                )

                point_cost_r = min(df[y][x+1] + dungeon[y][x], dungeon[y][x], 0)
                min_life_r = max(
                    -dungeon[y][x] + 1 if dungeon[y][x] < 0 else 1,
                    -point_cost_r + 1 if point_cost_r < 0 else 1
                )
                if min_life_d < min_life_r:
                    df[y][x] = point_cost_d
                else:
                    df[y][x] = point_cost_r

        return -df[0][0] + 1 if df[0][0] < 0 else 1

    def calculateMinimumHP_i(self, dungeon: List[List[int]]) -> int:
        """internet solution"""
        m, n = len(dungeon), len(dungeon[0])
        #use df with extra space "n+1"
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        #set first neighbors to 1
        dp[m-1][n] = dp[m][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        return dp[0][0]

    def calculateMinimumHP_2(self, dungeon: List[List[int]]) -> int:
        df = [[None] * len(l) for l in dungeon]

        df[-1][-1] = dungeon[-1][-1]
        for y in range(len(dungeon)-1, -1, -1):
            for x in range(len(dungeon[0])-1, -1, -1):
                if x == len(dungeon[0])-1 and y == len(dungeon)-1:
                    continue
                elif x == len(dungeon[0])-1:
                    point_cost = min(df[y+1][x] + dungeon[y][x], dungeon[y][x])
                    df[y][x] = 0 if point_cost > 0 else point_cost
                elif y == len(dungeon)-1:
                    point_cost = min(df[y][x+1] + dungeon[y][x], dungeon[y][x])
                    df[y][x] = 0 if point_cost > 0 else point_cost
                else:
                    point_cost_d = min(df[y+1][x] + dungeon[y][x], dungeon[y][x])
                    min_life_d = max(
                        -dungeon[y][x] + 1 if dungeon[y][x] < 0 else 1,
                        -point_cost_d + 1 if point_cost_d < 0 else 1
                    )

                    point_cost_r = min(df[y][x+1] + dungeon[y][x], dungeon[y][x])
                    min_life_r = max(
                        -dungeon[y][x] + 1 if dungeon[y][x] < 0 else 1,
                        -point_cost_r + 1 if point_cost_r < 0 else 1
                    )
                    if min_life_d < min_life_r:
                        df[y][x] = 0 if point_cost_d > 0 else point_cost_d
                    else:
                        df[y][x] = 0 if point_cost_r > 0 else point_cost_r

        return -df[0][0] + 1 if df[0][0] < 0 else 1

    def calculateMinimumHP_1(self, dungeon: List[List[int]]) -> int:
        df = [[None] * len(l) for l in dungeon]

        min_life = max(1, -dungeon[-1][-1] + 1)
        df[-1][-1] = (dungeon[-1][-1], min_life)
        for y in range(len(dungeon)-1, -1, -1):
            for x in range(len(dungeon[0])-1, -1, -1):
                if x == len(dungeon[0])-1 and y == len(dungeon)-1:
                    continue
                elif x == len(dungeon[0])-1:
                    point_cost = min(df[y+1][x][0] + dungeon[y][x], dungeon[y][x])
                    min_life = (max(
                        -dungeon[y][x] + 1 if dungeon[y][x] < 0 else 1,
                        -point_cost + 1 if point_cost < 0 else 1
                    ))
                    df[y][x] = (0 if point_cost > 0 else point_cost, min_life)
                elif y == len(dungeon)-1:
                    point_cost = min(df[y][x+1][0] + dungeon[y][x], dungeon[y][x])
                    min_life = (max(
                        -dungeon[y][x] + 1 if dungeon[y][x] < 0 else 1,
                        -point_cost + 1 if point_cost < 0 else 1
                    ))
                    df[y][x] = (0 if point_cost > 0 else point_cost, min_life)
                else:
                    point_cost_d = min(df[y+1][x][0] + dungeon[y][x], dungeon[y][x])
                    min_life_d = (max(
                        -dungeon[y][x] + 1 if dungeon[y][x] < 0 else 1,
                        -point_cost_d + 1 if point_cost_d < 0 else 1
                    ))

                    point_cost_r = min(df[y][x+1][0] + dungeon[y][x], dungeon[y][x])
                    min_life_r = (max(
                        -dungeon[y][x] + 1 if dungeon[y][x] < 0 else 1,
                        -point_cost_r + 1 if point_cost_r < 0 else 1
                    ))
                    if min_life_d < min_life_r:
                        df[y][x] = (0 if point_cost_d > 0 else point_cost_d, min_life_d)
                    else:
                        df[y][x] = (0 if point_cost_r > 0 else point_cost_r, min_life_r)

        return df[0][0][1]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.calculateMinimumHP(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7)
    do_test(1, [[0]], 1)
    do_test(2, [[-1]], 2)
    do_test(3, [[1]], 1)
    do_test(4, [[0, 1]], 1)
    do_test(5, [[0], [1]], 1)
    do_test(6, [[1, -3, 3], [0, -2, 0], [-3, -3, -3]], 3)
    do_test(7, [[1], [-2], [1]], 2)
    do_test(8, [[1, -2, 1]], 2)

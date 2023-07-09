import bisect
from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import os.path
import sys
input = sys.stdin.readline


MOD = 10**9+7
test = False


def i_int() -> int: return int(input())
def i_str() -> str: return input()[:-1]
def i_array_int() -> List[int]: return list(map(int, input().split()))
def i_array_str() -> List[str]: return i_str().split()
def i_set_int() -> Set[int]: return set(map(int, input().split()))
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


def solve():
    for _ in range(i_int()):
        grid = []
        for _ in range(3):
            grid.append(i_str())

        winner = None
        for r in grid:
            if r[0] == r[1] and r[1] == r[2] and r[0] != ".":
                winner = r[0]
        if winner:
            print(winner)
            continue

        for c in range(3):
            if grid[0][c] == grid[1][c] and grid[1][c] == grid[2][c] and grid[2][c] != ".":
                winner = grid[0][c]
        if winner:
            print(winner)
            continue

        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[2][2] != ".":
            winner = grid[0][0]
        if winner:
            print(winner)
            continue

        if grid[2][0] == grid[1][1] and grid[1][1] == grid[0][2] and grid[0][2] != ".":
            winner = grid[2][0]
        if winner:
            print(winner)
            continue
        print("DRAW")


testData = """5
+X+
OXO
OX.
O+.
+OX
X+O
.XO
OX.
+++
O.+
X.O
+..
.++
X.O
+..
""".split("\n")
# testData = list()
testDataPos = 0

if len(testData) > 1 and os.path.exists('localTestCheckFile.txt'):
    test = True

    def test_data_input():
        global testDataPos
        r = testData[testDataPos]
        testDataPos += 1
        return r + "\n"
    input = test_data_input


if __name__ == "__main__":
    solve()

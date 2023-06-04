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
def i_array_str() -> List[str]: i_str().split()
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


def solve_s():
    """sample solution"""
    n, q = i_array_int()
    a = i_array_int()

    dp = [0] * (n-1)
    for i in range(1, n-1):
        if a[i-1] >= a[i] and a[i] >= a[i+1]:
            dp[i] = 1
        dp[i] += dp[i-1]

    for _ in range(q):
        l, r = i_array_int()

        if l == r:
            print(1)
        else:
            print(r-l+1 - dp[r-2] + dp[l-1])


def solve():
    n, q = i_array_int()
    a = i_array_int()

    dp = [0] * (n+1)

    dp[1] = 1
    if n >= 2:
        dp[2] = 2

    for l in range(3, n+1):
        end = l - 1
        dp[l] = dp[l-1] + (0 if a[end-2] >= a[end-1] and a[end-1] >= a[end] else 1)

    for _ in range(q):
        l, r = i_array_int()
        if l == r:
            print(1)
            continue

        s = 0
        if dp[l-1] == dp[l]:
            s = 1
        if dp[l] == dp[l+1]:
            s += 1
        print(dp[r] - dp[l-1] + s)


def solve_f():
    """MEMORY_LIMIT_EXCEEDED"""
    n, q = i_array_int()
    a = i_array_int()

    dp = [[0] * n for _ in range(n)]

    for i in range(n-1):
        dp[2][i] = 2

    for l in range(3, n):
        for start in range(n-l+1):
            end = start + l - 1
            a1 = dp[l-1][start] + (0 if a[end-2] >= a[end-1] and a[end-1] >= a[end] else 1)
            a2 = dp[l-1][start+1] + (0 if a[start] >= a[start+1] and a[start+1] >= a[start+2] else 1)
            dp[l][start] = max(
                a1,
                a2
            )

    for _ in range(q):
        l, r = i_array_int()
        if l == r:
            print(1)
            continue

        print(dp[r-l+1][l-1])


testData = """9 9
1 2 4 3 3 5 6 2 1
1 3
1 4
2 5
6 6
3 7
7 8
1 8
8 8
4 6
""".split("\n")
# testData = """1 1
# 100
# 1 1
# """.split("\n")
# testData = """2 3
# 100 101
# 1 1
# 1 2
# 2 2
# """.split("\n")
# testData = """5 1
# 1 1 1 1 1
# 2 5
# testData = """5 7
# 1 1 0 1 1
# 1 2
# 2 3
# 3 4
# 4 5
# 1 5
# 2 5
# 3 5
# # # """.split("\n")
testData = """6 7
1 2 3 1 1 1 1
1 2
1 3
1 4
1 5
2 5
3 5
4 6
# # """.split("\n")
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

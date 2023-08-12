import bisect
from collections import defaultdict
import itertools
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


def cost(a) -> int:
    r = 0
    m = 0
    for i, n in enumerate(a):
        cur = (i+1)*n
        r += cur
        m = max(cur, m)
    return r-m


def solve():
    for _ in range(i_int()):
        n = i_int()
        a = [i for i in range(1, n+1)]
        resp = 0
        for i in range(n):
            tmp = a[:i] + [k for k in reversed(a[i:])]
            cur = cost(tmp)
            resp = max(resp, cur)
        print(resp)


testData = """5
2
4
3
10
20
""".split("\n")
# testData = """11
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# """.split("\n")
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

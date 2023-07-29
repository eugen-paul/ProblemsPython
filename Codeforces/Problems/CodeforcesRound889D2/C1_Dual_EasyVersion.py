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


def is_decreasing(a: List[int]) -> bool:
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return True
    return False


LIMIT = 50


def solve_pos(a: List[int]) -> List[Tuple[int, int]]:
    cnt = 0
    pos = 1
    resp = []
    while is_decreasing(a) and cnt <= LIMIT+1:
        if a[pos-1] > a[pos]:
            ma = max(a)
            cnt += 1
            resp.append((pos+1, a.index(ma)+1))
            a[pos] += ma
        else:
            pos += 1
    return resp


def solve_neg(a: List[int]) -> List[Tuple[int, int]]:
    cnt = 0
    pos = len(a)-2
    resp = []
    while is_decreasing(a) and cnt <= LIMIT+1 and pos >= 0:
        if a[pos] > a[pos+1]:
            mi = min(a)
            cnt += 1
            resp.append((pos+1, a.index(mi)+1))
            a[pos] += mi
        else:
            pos -= 1
    return resp


def solve():
    for _ in range(i_int()):
        n = i_int()
        a = i_array_int()
        if n == 1:
            print(0)
            continue

        positive = max(a) > 0

        if positive:
            resp = solve_pos(a.copy())
            if len(resp) > LIMIT and min(a) < 0:
                resp = solve_neg(a)
        else:
            resp = solve_neg(a)

        if len(resp) > LIMIT:
            raise RuntimeError()

        print(len(resp))
        if len(resp) == 0:
            continue
        for a, b in resp:
            print(a, b)


testData = """13
2
2 1
4
1 2 -10 3
5
2 1 1 1 1
8
0 0 0 0 0 0 0 0
5
1 2 -4 3 -10
10
11 12 13 14 15 -15 -16 -17 -18 -19
7
1 9 3 -4 -3 -2 -1
3
10 9 8
20
1 -14 2 -10 6 -5 10 -13 10 7 -14 19 -5 19 1 18 -16 -7 12 8
20
-15 -17 -13 8 14 -13 10 -4 11 -4 -16 -6 15 -4 -2 7 -9 5 -5 17
4
-5 -4 -5 -4
20
-1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20
20
1 -20 -1 -1 -1 -1 -1 -1 -1 -1 -1 -2 -3 -4 -5 -16 -17 -18 -19 -20
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

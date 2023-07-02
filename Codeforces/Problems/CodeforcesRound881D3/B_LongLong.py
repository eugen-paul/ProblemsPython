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
        _ = i_int()
        a = i_array_int()
        s = 0
        for c in a:
            s += abs(c)

        last = a[0]
        pos = 1 if last > 0 else 0
        neg = 1 if last < 0 else 0
        for i in range(1, len(a)):
            if a[i] > 0 and last <= 0:
                pos += 1
            elif a[i] < 0 and last >= 0:
                neg += 1
            if a[i] != 0:
                last = a[i]

        num = min(
            neg,
            1 + pos
        )
        print(s, num)


testData = """5
6
-1 7 -4 -2 5 -8
8
-1 0 0 -2 1 0 -3 0
5
2 -1 0 -3 -7
5
0 -17 0 1 0
4
-1 0 -2 -1
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

import bisect
from collections import defaultdict
from math import inf
import math
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
def i_set_int() -> Set[int]: return set(map(int, input().split()))
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


def solve():
    for _ in range(i_int()):
        _ = i_int()
        a = sorted(i_array_int())

        def check(a: List[int], m: int) -> int:
            start = a[0]
            cnt = 1
            for c in a:
                if c-start > 2*m:
                    cnt += 1
                    start = c
                    if cnt > 3:
                        return False
            return True

        l, r = 0, a[-1]
        while l <= r:
            m = (r+l) // 2
            if check(a, m):
                r = m-1
            else:
                l = m+1
        print(l)


testData = """14
6
1 2 3 4
6
7 7 9 9 9
6
1 7 7 9 9 9
6
5 4 2 1 30 60
9
14 19 37 59 1 4 4 98 73
1
2
6
3 10 1 17 15 11
6
1 7 7 8 9 9
7
1 2 7 7 8 9 9
8
1 2 3 4 5 6 7 8
9
1 2 3 4 5 6 7 8 9
11
11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
10
11 12 13 14 15 16 17 18 19 20
5
6 6 19 1 10
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

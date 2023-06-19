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
        A, B, C, k = i_array_int()

        a_min = 10 ** (A-1)
        a_max = 10 ** A - 1
        b_min = 10 ** (B-1)
        b_max = 10 ** B - 1
        c_min = 10 ** (C-1)
        c_max = 10 ** C - 1

        pos = 1

        ok = False
        for a in range(a_min, a_max+1):
            if c_min <= a + b_min and a + b_min <= c_max:
                b_start = b_min
            else:
                b_start = c_min - a
            if a + b_max <= c_max:
                b_end = b_max
            else:
                b_end = c_max - a
            if b_start > b_max or b_end < b_min:
                continue

            if pos + b_end - b_start + 1 <= k:
                pos += b_end - b_start + 1
            else:
                b = b_start + k-pos
                print(a, "+", b, "=", a+b)
                ok = True
                break

        if not ok:
            print(-1)


testData = """8
1 1 1 9
2 2 3 1
2 2 1 1
1 5 6 42
1 6 6 10000000
5 5 6 3031568815
6 6 6 1000000000000
2 1 3 40
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

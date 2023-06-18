import bisect
from collections import defaultdict
from math import ceil, inf
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
        n, k, g = i_array_int()

        if n == 1:
            print(0)
            continue

        li = ceil(g / 2)
        tmp = li-1

        silb = k*g
        x = max(0, silb - (n-1)*tmp)
        r = x % g
        if r >= li:
            to_pay = x+g-r
        else:
            to_pay = x-r
            

        print(k*g - to_pay)


testData = """6
3 3 100
2 1 14
91 2 13
36 16 6
73 8 22
10 10 1
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

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
def i_array_str() -> List[str]: return i_str().split()
def i_set_int() -> Set[int]: return set(map(int, input().split()))
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


def solve():
    for _ in range(i_int()):
        n = i_int()
        if n == 1:
            print("a")
            continue

        for i in range(2, 1001):
            if n % i != 0:
                break

        resp = []
        for j in range(i):
            resp.append(chr(ord("a")+j))
        while len(resp) < n:
            resp.extend(resp)
        if len(resp) > n:
            resp = resp[:n]
        print("".join(resp))


testData = """7
4
2
1
6
7
32
420
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

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


def solve():
    for _ in range(i_int()):
        a = i_str()

        if a == "^":
            print(1)
            continue
        resp = 0
        if a[0] == "_":
            resp += 1
        if a[-1] == "_":
            resp += 1
        b = a.split("^")
        for sub in b:
            if len(sub) > 1:
                resp += len(sub)-1

        print(resp)


def solve_2():
    for _ in range(i_int()):
        a = i_str()

        if a == "^":
            print(1)
            continue

        resp = 0 if a[0] == "^" else 1
        last = " "
        for c in a:
            if last == "_" and c == "_":
                resp += 1
            last = c
        if last == "_":
            resp += 1

        print(resp)


testData = """7
^______^
___^_^^^_^___^
^_
^
^_^^^^^_^_^^
___^^
_
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

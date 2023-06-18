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
def i_set_int() -> Set[int]: return set(map(int, input().split()))
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


def solve():
    for _ in range(i_int()):
        n = i_int()
        a = i_array_int()

        cnt_neg = a.count(-1)
        cnt_pos = n - cnt_neg

        resp = 0

        if cnt_neg <= cnt_pos and cnt_neg % 2 == 0:
            resp = 0
        elif cnt_neg <= cnt_pos and cnt_neg % 1 == 0:
            resp = 1
        elif cnt_neg > cnt_pos:
            resp = (cnt_neg - cnt_pos) // 2
            if cnt_neg - resp > cnt_pos + resp:
                resp += 1
            if (cnt_neg - resp) % 2 == 1:
                resp += 1

        print(resp)


testData = """7
4
-1 -1 1 -1
5
-1 -1 -1 1 1
4
-1 1 -1 1
3
-1 -1 -1
5
1 1 1 1 1
1
-1
2
-1 -1
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

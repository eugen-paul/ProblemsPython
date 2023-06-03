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
        n = i_int()
        a = i_array_int()
        if a[-1] == 1:
            print("NO")
            continue

        resp = Deque()
        for i, n in enumerate(a):
            if n == 1:
                continue
            tmp = Deque()
            k = i - 1
            while k >= 0 and a[k] == 1:
                tmp.append(0)
                k -= 1
            tmp.append(len(tmp))
            resp.appendleft(tmp)

        print("YES")
        for q in resp:
            print(*q, end=" ")
        print("")

def solve_s():
    """too slow"""
    for _ in range(i_int()):
        n = i_int()
        a = i_array_int()
        if a[-1] == 1:
            print("NO")
            continue

        resp = Deque()
        for i, n in enumerate(a):
            if n == 1:
                continue
            tmp = Deque()
            k = i - 1
            while k >= 0 and a[k] == 1:
                tmp.append(0)
                k -= 1
            tmp.append(len(tmp))
            resp = tmp + resp

        print("YES")
        print(*resp)


testData = """4
5
1 1 0 0 0
1
1
3
0 1 1
6
1 0 0 1 1 0
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

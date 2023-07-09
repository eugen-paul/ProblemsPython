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
        n, m, h = i_array_int()

        pr: List[List[int]] = []
        for _ in range(n):
            pr.append(i_array_int())

        result = []
        for i, r in enumerate(pr):
            r.sort()
            s = 0
            t = 0
            cnt = 0
            for c in r:
                if s+c <= h:
                    cnt += 1
                    t = t + s + c
                    s = s + c
                else:
                    break
            result.append((m-cnt, t, i))

        result.sort()

        for i, c in enumerate(result):
            if c[2] == 0:
                print(i+1)


testData = """5
3 3 120
20 15 110
90 90 100
40 40 40
2 1 120
30
30
1 3 120
10 20 30
3 2 27
8 9
10 7
10 8
3 3 15
7 2 6
7 5 4
1 9 8
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

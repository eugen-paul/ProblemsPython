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

        o, t, m = 0, 0, 0
        for i, c in enumerate(a):
            if c == 1:
                o = i
            elif c == 2:
                t = i
            elif c == n:
                m = i

        if abs(o-t) != 1:
            if o < t:
                print(o + 2, m+1)
            else:
                print(o, m+1)
        else:
            if abs(o-m) == 1:
                print(o+1, m+1)
            else:
                if o < t and o < m:
                    print(t+1, m+1)
                elif m < o and t < o:
                    print(t+1, m+1)
                else:
                    print(o+1, m+1)


testData = """8
3
1 2 3
3
1 3 2
5
1 3 2 5 4
6
4 5 6 1 2 3
9
8 7 6 3 2 1 4 5 9
10
7 10 5 1 9 8 3 2 6 4
10
8 5 10 9 2 1 3 4 6 7
10
2 3 5 7 10 1 8 6 4 9
""".split("\n")
# testData = """4
# 5
# 1 2 3 4 5
# 5
# 5 2 1 3 4
# 5
# 5 3 1 2 4
# 5
# 4 2 1 3 5
# """.split("\n")
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

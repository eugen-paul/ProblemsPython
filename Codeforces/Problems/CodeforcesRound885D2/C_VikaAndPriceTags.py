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


def param(x, y) -> int:
    cnt = 0
    while x != 0:
        if y != 0:
            x %= 2 * y
        x, y = y, abs(x-y)
        cnt += 1
    return cnt % 3


def solve():
    for _ in range(i_int()):
        _ = i_int()
        a = i_array_int()
        b = i_array_int()

        p = None
        ok = True
        for x, y in zip(a, b):
            if x == 0 and y == 0:
                continue
            tmp = param(x, y)
            if p is None:
                p = tmp
            elif p != tmp:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")


testData = """9
4
0 0 0 0
1 2 3 4
3
1 2 3
1 2 3
2
1 2
2 1
6
100 23 53 11 56 32
1245 31 12 6 6 6
7
1 2 3 4 5 6 7
7 6 5 4 3 2 1
3
4 0 2
4 0 2
3
2 5 2
1 3 4
2
6 1
4 2
2
0 0
0 3
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

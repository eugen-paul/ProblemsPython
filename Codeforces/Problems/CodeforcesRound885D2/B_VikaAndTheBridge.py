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
        n, _ = i_array_int()
        c = i_array_int()

        m = dict()

        for i, color in enumerate(c):
            if color in m:
                last_pos = m[color][0]
                cur_diff = i-last_pos-1
                last_dif = m[color][1][0]
                pre_dif = m[color][1][1]
                m[color] = [i, sorted([cur_diff, last_dif, pre_dif], reverse=True)]
            else:
                m[color] = [i, (i, 0, 0)]

        for k in m.keys():
            last_pos = m[k][0]
            cur_diff = n-last_pos-1
            last_dif = m[k][1][0]
            pre_dif = m[k][1][1]
            m[k] = [n, sorted([cur_diff, last_dif, pre_dif], reverse=True)]

        steps = [(v[0], v[1]) for _, v in m.values()]
        steps.sort(key = lambda x: max(x[0] // 2, x[1]))
        print(max(steps[0][0] // 2, steps[0][1]))


testData = """5
5 2
1 1 2 1 1
7 3
1 2 3 3 3 2 1
6 6
1 2 3 4 5 6
8 4
1 2 3 4 2 3 1 4
3 1
1 1 1
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

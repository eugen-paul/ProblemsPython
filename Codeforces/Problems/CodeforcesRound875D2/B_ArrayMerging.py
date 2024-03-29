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
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


def get_l(a):
    m = defaultdict(lambda: 0)
    last = -1
    cnt = 0
    for i in a:
        if last != i:
            cnt = 1
            last = i
        else:
            cnt += 1
        if m[i] < cnt:
            m[i] = cnt
    return m


def solve():
    for _ in range(i_int()):
        n = i_int()
        a = i_array_int()
        b = i_array_int()

        a_l = get_l(a)
        b_l = get_l(b)

        resp = 0
        for i in a:
            resp = max(resp, a_l[i] + b_l[i])
        for i in b:
            resp = max(resp, a_l[i] + b_l[i])

        print(resp)


testData = """5
1
2
2
3
1 2 3
4 5 6
2
1 2
2 1
5
1 2 2 2 2
2 1 1 1 1
6
2 2 1 3 3 3
2 1 3 1 3 4
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

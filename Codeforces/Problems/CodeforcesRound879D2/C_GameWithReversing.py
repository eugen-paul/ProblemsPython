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
        _ = i_int()
        S = i_str()
        T = i_str()

        delta = 0
        for a, b in zip(S, T):
            if a != b:
                delta += 1

        delta_rev = 0
        for a, b in zip(S, reversed(T)):
            if a != b:
                delta_rev += 1

        if delta == 0:
            print(0)
            continue
        if delta_rev == 0:
            print(2)
            continue

        moves = delta-1
        resp = delta + moves
        if moves % 2 == 1:
            resp += 1

        delta = delta_rev - 1
        moves = max(0, delta-1)
        tmp = delta + moves
        if moves % 2 == 1:
            tmp += 1
        resp = min(tmp+2, resp)

        print(resp)


testData = """9
13
aaabbbbbcfgtz
bbbbbbbbcfgtz
3
qab
qcd
5
abcde
abxde
5
hello
olleo
2
ab
cd
7
aaaaaaa
abbbbba
1
q
q
6
yoyoyo
oyoyoy
8
abcdefgh
hguedfbh
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

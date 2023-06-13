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
        s = [ord(c)-ord("A") for c in i_str()]

        def comp(s) -> int:
            val = [1, 10, 100, 1_000, 10_000]
            pos = [True, True, True, True, True]
            full = 0
            for c in reversed(s):
                if pos[c]:
                    full += val[c]
                else:
                    full -= val[c]
                for i in range(c):
                    pos[i] = False
            return full

        # Get first and last position of each character
        first = [-1, -1, -1, -1, -1]
        last = [-1, -1, -1, -1, -1]
        for i, c in enumerate(s):
            if first[c] == -1:
                first[c] = i
            last[c] = i

        resp = -inf
        to_check = {*first, *last}

        # Try to replace each first and last appearance of each character.
        for sr in to_check:
            if sr == -1:
                continue
            tmp = s[sr]
            for tr in range(5):
                s[sr] = tr
                resp = max(resp, comp(s))
            s[sr] = tmp

        print(resp)


testData = """8
DAAABDCA
AB
ABCDEEDCBA
DDDDAAADDABECD
A
BDDEAEBDDDAAADCBDDDACBDCCBAADCBCBDDDACEBDAAACDDABA
EDDDDDDDDDDDE
DDDDDDDDDDDDE
""".split("\n")
testData = """2
DDDDDDDDDDDDDDDDDDDE
EEEEE
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

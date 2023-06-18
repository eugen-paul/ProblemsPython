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
        n = i_int()
        l = i_array_int()
        l.sort()
        c = Counter(l)
        last_k = -1
        last_v = inf
        ok = True
        for k, v in sorted(c.items()):
            if k != last_k + 1 or last_v < v:
                ok = False
                break
            last_k = k
            last_v = v

        if ok:
            print("YES")
        else:
            print("NO")


testData = """5
6
0 1 2 0 1 0
9
0 0 0 0 1 1 1 2 2
3
0 0 2
1
99
5
0 1 2 3 4
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

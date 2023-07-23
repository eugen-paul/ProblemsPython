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
        n, k = i_array_int()

        def fib_len(t) -> int:
            a, b, l = t, n, 2
            while a >= 0 and a <= b:
                a, b = b-a, a
                l += 1
            return l-1

        resp = 0
        
        for i in range(n, math.ceil(n/2)-1,-1):
            if fib_len(i) >= k:
                resp+=1
        
        print(resp)
        


testData = """8
22 4
3 9
55 11
42069 6
69420 4
69 1434
1 3
1 4
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

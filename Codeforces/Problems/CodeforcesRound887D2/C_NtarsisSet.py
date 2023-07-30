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
    """
                    1                   2
    1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 

    1 X 3   5 6 7
      1   X       3   5 6 7
          1         X       3   5 6 7
                    1         X       3   5 6 7

    k=1:
    x 1

    k=2:
      x   1
    x x   1

    k=3:
          x         1
    x     x       x 1
    x x x x x x x x 1

    k=4:
                    x         1
              x     x       x 1
              x x x x x x x x 1
    x x x x x x x x x x x x x 1
    """
    for _ in range(i_int()):
        n, k = i_array_int()
        a = i_array_int()

        if (a[0] != 1):
            print(1)
            continue

        pos = 1  # counter of are missing number we are looking for
        x = 1    # min counter of "x" that will be added to response array each round
        for _ in range(k):
            for x in range(x, n+1):  # try all numbers from x to n to find next missing number in a
                if x == n:           # there are no missing numbers more
                    break
                if a[x] > pos+x:     # we are looking for "pos" missing number
                    break
            pos += x

        print(pos)


def solve_s():
    """sample solution"""
    for _ in range(i_int()):
        n, k = i_array_int()
        a = i_array_int()

        j, x = 0, 1
        while k != 0:
            while j < n and a[j] <= x+j:
                j += 1
            x += j
            k -= 1
        print(x)


def solve_1():
    """internet solution"""
    for _ in range(i_int()):
        n, k = i_array_int()
        a = i_array_int()

        lb = 1
        ub = n*k+10
        while ub-lb > 1:
            mid = (lb+ub)//2
            tmp = mid
            for _ in range(k):
                tmp -= bisect.bisect(a, tmp)
                if tmp < 0:
                    break
            if tmp <= 0:
                lb = mid
            else:
                ub = mid
        print(ub)


def solve_2():
    """internet solution"""
    t = int(input())
    for _ in range(t):
        _, k = i_array_int()
        a = i_array_int()

        if (a[0] != 1):
            print(1)
            continue

        z = 1
        dz = 1
        for _ in range(k):
            z += dz
            while bisect.bisect(a, z) > dz:
                dz += 1
                z += 1
        print(z)


testData = """7
5 1
1 2 4 5 6
5 3
1 3 5 6 7
4 1000
2 3 4 5
9 1434
1 4 7 9 12 15 17 18 20
10 4
1 3 5 7 9 11 13 15 17 19
10 6
1 4 7 10 13 16 19 22 25 28
10 150000
1 3 4 5 10 11 12 13 14 15
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

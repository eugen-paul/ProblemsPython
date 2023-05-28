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


def solve():
    for _ in range(int(input())):
        n = int(input())
        l = i_array_int()

        ans = -1
        # iterate over the number of liars
        for liars in range(n):
            # count the actual number of liars
            liars_cnt = 0
            for person_says in l:
                if liars < person_says:
                    liars_cnt += 1
            if liars == liars_cnt:
                ans = liars
                break

        print(ans)


testData = """7
2
1 2
2
2 2
2
0 0
1
1
1
0
5
5 5 3 3 5
6
5 3 6 6 3 5
""".split("\n")
# testData = list()
testDataPos = 0

if len(testData) > 1 and os.path.exists('localTestCheckFile.txt'):
    test = True

    def test_data_input():
        global testDataPos
        r = testData[testDataPos]
        testDataPos += 1
        return r
    input = test_data_input


if __name__ == "__main__":
    solve()

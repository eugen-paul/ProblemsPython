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
        n = i_int()
        q = i_array_int()
        a = Deque()
        a.append(1)
        first = q[0]
        last = q[0]
        br = False

        for i in range(1, len(q)):
            cur = q[i]
            if cur >= last and not br:
                a.append(1)
                last = cur
            elif cur < last and not br:
                if first >= cur:
                    br = True
                    last = cur
                    a.append(1)
                else:
                    a.append(0)
            elif cur >= last and br:
                if first >= cur:
                    last = cur
                    a.append(1)
                else:
                    a.append(0)
            else:  # cur < last and br
                a.append(0)

        print("".join(str(i) for i in a))


testData = """4
9
3 7 7 9 2 4 6 3 4
5
1 1 1 1 1
5
3 2 1 2 3
9
3 7 8 4 2 3 3 3 3
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

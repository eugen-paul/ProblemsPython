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
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


def solve():
    for _ in range(i_int()):
        n = i_int()

        m = defaultdict(list)
        for _ in range(n):
            a, b = i_array_int()
            m[a].append(b)

        resp = 0
        for a, bs in m.items():
            bs.sort(reverse=True)
            resp += sum(bs[:a])
        print(resp)


def solve_s():
    """too slow"""
    for _ in range(i_int()):
        n = i_int()

        m = []
        for _ in range(n):
            a, b = i_array_int()
            m.append((a, -b))
        m.sort()

        nxt = 1
        on = []
        resp = 0
        for i, n in enumerate(m):
            a, b = n
            if a < nxt:
                continue
            resp += -b
            on += [a]
            pos = bisect.bisect_right(on, len(on))
            nxt = max(nxt, len(on)+1)
            on = on[pos:]

        print(resp)


testData = """4
4
2 2
1 6
1 10
1 13
5
3 4
3 1
2 5
3 2
3 3
6
1 2
3 4
1 4
3 4
3 5
2 3
1
1 1
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

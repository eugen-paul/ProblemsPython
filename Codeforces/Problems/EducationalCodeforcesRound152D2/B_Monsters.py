import bisect
from collections import defaultdict
import heapq
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
        n, k = i_array_int()
        a = i_array_int()
        c = []
        for i, v in enumerate(a):
            if v % k != 0:
                c.append((v % k - k, v // k + 1, i))
            else:
                c.append((v % k, v // k, i))

        c.sort(key=lambda x: (-x[0], x[2]))
        resp = [i+1 for _, _, i in c]
        print(*resp)


def solve_s():
    # too slow
    for _ in range(i_int()):
        n, k = i_array_int()
        a = i_array_int()

        h = []
        for i, c in enumerate(a):
            heapq.heappush(h, (-c, i))

        while h[0][0] < 0:
            cur, nr = heapq.heappop(h)
            heapq.heappush(h, (cur+k, nr))

        resp = []
        while h:
            resp.append((heapq.heappop(h)))
        # resp.sort(key=lambda x: x[1])
        resp = [i+1 for _, i in resp]
        print(*resp)


testData = """3
3 2
1 2 3
2 3
1 1
4 3
2 8 3 5
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

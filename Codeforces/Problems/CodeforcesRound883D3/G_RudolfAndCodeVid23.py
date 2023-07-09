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
        _, m = i_array_int()

        start = int(i_str(), base=2)
        medicines = []
        for _ in range(m):
            day = i_int()
            cur = int(i_str(), base=2)
            nxt = int(i_str(), base=2)
            medicines.append((day, cur, nxt))

        q = []
        heapq.heapify(q)
        heapq.heappush(q, (0, start))

        found = False
        SEEN = set()
        while q:
            cost, pos = heapq.heappop(q)
            if pos == 0:
                print(cost)
                found = True
                break
            if pos in SEEN:
                continue
            SEEN.add(pos)
            for day, med, neg in medicines:
                if med & pos == 0:
                    continue
                nn = (med | pos) ^ med
                nn |= neg
                if nn not in SEEN:
                    heapq.heappush(q, (day+cost, nn))

        if not found:
            print("-1")


testData = """4
5 4
10011
3
10000
00110
3
00101
00000
3
01010
00100
5
11010
00100
4 1
0000
10
1011
0100
2 2
11
2
10
01
3
01
10
2 3
11
3
01
10
3
10
00
4
10
01
""".split("\n")
testData = """1
1 5
1
4
1
0
5
0
1
3
1
0
3
1
0
4
1
0
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

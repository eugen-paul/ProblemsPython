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
        p = []
        for _ in range(n):
            d = i_array_int()
            p.append(d)
        p.sort(key=lambda x: (x[2], x[3]))
        pp = []
        cur = p[0]
        for i in range(1, len(p)):
            cc = p[i]
            if cur[3] >= cc[2]:
                cur = [
                    min(cc[0], cur[0]),
                    max(cc[1], cur[1]),
                    cur[2],
                    max(cc[3], cur[3])
                ]
            else:
                pp.append([cur[0], cur[3], cur[2], cur[3]])
                cur = cc
        pp.append(cur)

        pp.sort(key=lambda x: x[0])
        ppp = []
        cur = pp[0]
        for i in range(1, len(pp)):
            cc = pp[i]
            if cur[1] >= cc[0]:
                cur = [
                    min(cc[0], cur[0]),
                    max(cc[1], cur[1]),
                    cur[2],
                    max(cc[3], cur[3])
                ]
            else:
                ppp.append([cur[0], cur[3], cur[2], cur[3]])
                cur = cc
        ppp.append(cur)

        _ = i_int()
        x = i_array_int()
        resp = []
        for i in x:
            l, r = 0, len(ppp)-1
            while l <= r:
                m = (l+r)//2
                if ppp[m][1] >= i:
                    r = m-1
                else:
                    l = m+1
            posible = l
            best = i
            for l in range(max(0, posible-1), min(len(ppp), posible+2)):
                if ppp[l][0] <= i and i <= ppp[l][1]:
                    best = max(best, ppp[l][3])
            resp.append(best)
        print(*resp)


testData = """5
3
6 17 7 14
1 12 3 8
16 24 20 22
6
10 2 23 15 28 18
3
3 14 7 10
16 24 20 22
1 16 3 14
9
2 4 6 8 18 23 11 13 15
2
1 4 2 3
3 9 6 7
3
4 8 1
5
18 24 18 24
1 8 2 4
11 16 14 14
26 32 28 30
5 10 6 8
9
15 14 13 27 22 17 31 1 7
6
9 22 14 20
11 26 13 24
21 33 22 23
21 33 25 32
1 6 3 4
18 29 20 21
8
11 23 16 5 8 33 2 21
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

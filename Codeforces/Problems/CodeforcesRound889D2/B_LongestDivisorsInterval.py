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


# def get_prims(n: int) -> Set[int]:
#     resp = set()
#     sq = math.ceil(math.sqrt(n))
#     for p in range(2, sq+1):
#         if n % p == 0:
#             resp.add(p)
#             n //= p
#             while n % p == 0:
#                 n //= p
#         if p >= sq:
#             break
#     resp.add(n)
#     return resp


def solve():
    for _ in range(i_int()):
        n = i_int()
        if n % 2 == 1:
            print(1)
            continue

        pow2 = 2
        resp = 2
        tmp = n
        while tmp % 2 == 0:
            tt = pow2 - 1
            tmp_cnt = 0
            while n % tt == 0:
                tmp_cnt += 1
                tt += 1
            resp = max(resp, tmp_cnt)
            tmp = tmp // 2

        print(resp)


testData = """10
1
40
990990
4204474560
169958913706572972
365988220345828080
387701719537826430
620196883578129853
864802341280805662
1000000000000000000
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

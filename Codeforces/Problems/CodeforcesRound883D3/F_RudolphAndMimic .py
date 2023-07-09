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


def get_mim(c1: Counter, c2: Counter):
    c3 = c2-c1
    for k, _ in c3.items():
        return k


def solve():
    for _ in range(i_int()):
        _ = i_array_int()

        a1 = i_array_int()
        c1 = Counter(a1)
        print("- 0", flush=True)

        def step(prev_cnt: Counter) -> Tuple[bool, Counter]:
            a2 = i_array_int()
            c2 = Counter(a2)
            if c2 != prev_cnt:
                mm = get_mim(prev_cnt, c2)
                to_del = [i+1 for i, v in enumerate(a2) if v != mm]
                if len(to_del) == len(a2)-1:
                    print("!", a2.index(mm)+1, flush=True)
                    return (True, None)
                else:
                    if to_del:
                        print("-", len(to_del), *to_del, flush=True)
                    else:
                        print("- 0", flush=True)
                    v = c2[mm]
                    c2 = Counter()
                    c2[mm] = v
            else:
                print("- 0", flush=True)
            return (False, c2)

        r = step(c1)
        while not r[0]:
            r = step(r[1])


testData = """""".split("\n")
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

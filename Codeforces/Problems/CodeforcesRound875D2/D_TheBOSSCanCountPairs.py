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
def i_array_str() -> List[str]: i_str().split()
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


def solve():
    for _ in range(i_int()):
        n = i_int()
        A = i_array_int()
        B = i_array_int()

        m = defaultdict(list)
        for a, b in zip(A, B):
            m[a].append(b)

        A = sorted(list(set(A)))

        cnt = [0] * (n+1)
        ans = 0

        start = 0
        end = bisect.bisect_right(A, math.ceil(math.sqrt(2*n)))

        # Since ai*aj<=2*n, then min(ai,aj)<=sqrt(2*n)
        for i in range(start, end):
            # Firstly, we'll count the number of good pairs (i,j) such that ai=aj.
            a = A[i]
            for b in m[a]:
                t = a*a - b
                if 0 <= t <= n:
                    ans += cnt[t]
                cnt[b] += 1
            # The remaining good pairs will have ai != aj. Since i*j <= 2*n, then j <= 2*n//i
            lim = math.ceil(2*n//a)
            pos_lim = bisect.bisect_right(A, lim)
            for j in range(i+1, pos_lim):
                aj = A[j]
                for b in m[aj]:
                    t = a*aj - b
                    if 0 <= t <= n:
                        ans += cnt[t]
            for b in m[a]:
                cnt[b] -= 1

        print(ans)


def solve_4():
    """other sample solution"""
    for _ in range(i_int()):
        n = i_int()
        A = i_array_int()
        B = i_array_int()

        m = defaultdict(list)
        for a, b in zip(A, B):
            m[a].append(b)

        cnt = [0] * (n+1)
        ans = 0

        # Since ai*aj<=2*n, then min(ai,aj)<=sqrt(2*n)
        for i in range(1, math.ceil(math.sqrt(2*n)) + 1):
            # Firstly, we'll count the number of good pairs (i,j) such that ai=aj.
            for b in m[i]:
                t = i*i - b
                if 0 <= t <= n:
                    ans += cnt[t]
                cnt[b] += 1
            # The remaining good pairs will have ai != aj. Since i*j <= 2*n, then j <= 2*n//i
            lim = math.ceil(2*n//i)
            for j in range(i+1, lim+1):
                for b in m[j]:
                    t = i*j - b
                    if 0 <= t <= n:
                        ans += cnt[t]
            for b in m[i]:
                cnt[b] -= 1

        print(ans)


def solve_3():
    """sample solution with editions"""
    for _ in range(i_int()):
        n = i_int()

        c = [(x, y) for x, y in zip(i_array_int(), i_array_int())]
        c.sort()

        A = [x[0] for x in c]
        B = [x[1] for x in c]

        cnt = [0] * (n + 1)
        pr = 0
        ans = 0
        q = Deque()
        end_a = math.ceil(math.sqrt(2*n))

        for i in range(n):
            a, b = A[i], B[i]
            if pr != a:
                pr = a

                if a > end_a:
                    # global end -> a**2 is always <= 2*n
                    break

                while q:
                    cnt[q.pop()] = 0

                lim = 2 * n // a
                for j in range(i + 1, n):
                    if A[j] > lim:
                        # local end -> a1*a2 is always <= 2*n
                        break
                    t = a * A[j] - B[j]
                    if t >= 0 and t <= n:
                        cnt[t] += 1
                        if cnt[t] == 1:
                            q.append(t)

            ans += cnt[b]

            if i + 1 < n:
                t = a * A[i + 1] - B[i + 1]
                if t >= 0 and t <= n:
                    cnt[t] -= 1

        print(ans)


def solve_2():
    """sample solution with editions"""
    for _ in range(i_int()):
        n = i_int()

        a = i_array_int()
        b = i_array_int()

        c = [(x, y) for x, y in zip(a, b)]
        c.sort()

        a = [x[0] for x in c]
        b = [x[1] for x in c]

        cnt = [0] * (n + 1)
        pr = 0
        ans = 0

        for i in range(n):
            if pr != a[i]:
                pr = a[i]

                if pr * pr > 2 * n:
                    # global end -> a**2 is always <= 2*n
                    break

                cnt = [0] * (n + 1)
                lim = 2 * n // pr
                for j in range(i + 1, n):
                    if a[j] > lim:
                        # local end -> a1*a2 is always <= 2*n
                        break
                    t = a[i] * a[j] - b[j]
                    if t >= 0 and t <= n:
                        cnt[t] += 1

            ans += cnt[b[i]]

            if i + 1 < n:
                t = a[i] * a[i + 1] - b[i + 1]
                if t >= 0 and t <= n:
                    cnt[t] -= 1

        print(ans)


def solve_1():
    """sample solution with editions: still too slow"""
    for _ in range(i_int()):
        n = i_int()

        ta = i_array_int()
        tb = i_array_int()

        a = [(x, y) for x, y in zip(ta, tb)]
        a.sort()

        cnt = [0] * (n + 1)
        pr = 0
        ans = 0

        for i in range(n):
            if pr != a[i][0]:
                pr = a[i][0]

                if pr * pr > 2 * n:
                    # global end -> a**2 is always <= 2*n
                    break

                cnt = [0] * (n + 1)
                lim = 2 * n // pr
                for j in range(i + 1, n):
                    if a[j][0] > lim:
                        # local end -> a1*a2 is always <= 2*n
                        break
                    #      a_i  *  a_j    - b_j
                    t = a[i][0] * a[j][0] - a[j][1]
                    if t >= 0 and t <= n:
                        cnt[t] += 1

            ans += cnt[a[i][1]]

            if i + 1 < n:
                t = a[i][0] * a[i + 1][0] - a[i + 1][1]
                if t >= 0 and t <= n:
                    cnt[t] -= 1

        print(ans)


def solve_s():
    """sample solution: too slow :("""
    for _ in range(int(input())):
        n = int(input())

        ta = list(map(int, input().split()))
        tb = list(map(int, input().split()))

        a = [(x, y) for x, y in zip(ta, tb)]
        a.sort()

        cnt = [0] * (2 * n + 1)
        pr = 0
        ans = 0

        for i in range(n):
            if pr != a[i][0]:
                pr = a[i][0]

                if pr * pr > 2 * n:
                    break

                cnt = [0] * (2 * n + 1)
                for j in range(i + 1, n):
                    t = a[i][0] * a[j][0] - a[j][1]
                    if t >= 0 and t <= 2 * n:
                        cnt[t] += 1

            ans += cnt[a[i][1]]

            if i + 1 < n:
                t = a[i][0] * a[i + 1][0] - a[i + 1][1]
                if t >= 0 and t <= 2 * n:
                    cnt[t] -= 1

        print(ans)


testData = """3
3
2 3 2
3 3 1
8
4 2 8 2 1 2 7 5
3 5 8 8 1 1 6 5
8
4 4 8 8 8 8 8 8
8 8 8 8 8 8 8 8
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

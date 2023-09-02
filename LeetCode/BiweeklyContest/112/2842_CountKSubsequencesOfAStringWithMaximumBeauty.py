from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        mod = 1000000007
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        count = sorted([c for c in count if c], reverse=True)
        if len(count) < k:
            return 0
        ans = 1
        if len(count) == k:
            for i in range(k):
                ans = ans * count[i] % mod
            return ans
        mi = count[k]
        m = k
        for i in range(k):
            if count[i] > mi:
                ans = ans * count[i] % mod
                m -= 1
            else:
                break
        n = count.count(mi)
        c = math.comb(n, m) % mod
        ans = ((mi**m % mod) * ans * c) % mod
        return ans

    def countKSubsequencesWithMaxBeauty_i(self, s: str, k: int) -> int:
        """internet solution"""
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        count = sorted([c for c in count if c], reverse=True)
        if len(count) < k:
            return 0
        ans = 1
        mod = 1000000007
        for i in range(k):
            ans = ans * count[i] % mod
        n = count.count(count[k - 1])
        m = count[:k].count(count[k - 1])
        for i in range(1, n + 1):
            ans = ans * i % mod
        for i in range(1, m + 1):
            ans = ans * pow(i, mod - 2, mod) % mod
        for i in range(1, n - m + 1):
            ans = ans * pow(i, mod - 2, mod) % mod
        return ans

    def countKSubsequencesWithMaxBeauty_slow(self, s: str, k: int) -> int:
        """TLE"""
        mod = 10**9+7
        b = defaultdict(int)
        for c in s:
            b[c] += 1

        s1 = list(set(s))
        if k > len(s1):
            return 0
        s1.sort(key=lambda x: b[x])
        s1 = s1[::-1]
        beauty = 0
        for c in s1[:k]:
            beauty += b[c]

        def get_cost(se: frozenset) -> int:
            r = 0
            for c in se:
                r += b[c]
            return r

        @cache
        def solve(pos: int, se: frozenset) -> int:
            if len(se) == k:
                if get_cost(se) == beauty:
                    return 1
                return 0
            if pos == len(s):
                return 0
            cnt = solve(pos+1, se)
            if s[pos] not in se:
                cnt = (cnt + solve(pos, frozenset(se.union(*s[pos])))) % mod
            return cnt

        return solve(0, frozenset())


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.countKSubsequencesWithMaxBeauty(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "bcca", 2, 4)
    do_test(1, "abbcd", 4, 2)
    do_test(2, "abbbdd", 2, 6)
    do_test(3, "abbbddd", 2, 9)
    do_test(4, "abbbdddd", 2, 12)
    do_test(5, "abbbddddb", 2, 16)
    do_test(6, "abbbddddbb", 2, 20)
    do_test(7, "lelxul", 1, 3)
    do_test(8, "ci", 1, 2)
    do_test(9, "jyuhiyzjuk", 2, 12)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

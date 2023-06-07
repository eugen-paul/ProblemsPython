from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        A = str(bin(a))[2:]
        B = str(bin(b))[2:]
        C = str(bin(c))[2:]

        A = "0"*(32-len(A)) + A
        B = "0"*(32-len(B)) + B
        C = "0"*(32-len(C)) + C

        resp = 0
        for a, b, c in zip(A, B, C):
            if a == b and b == c:
                continue
            if c == "0":
                resp += a == "1"
                resp += b == "1"
                continue
            if c == "1":
                resp += a == b

        return resp

    def minFlips_s(self, a: int, b: int, c: int) -> int:
        """sample solution"""
        answer = 0
        while a or b or c:
            if c & 1:
                answer += 0 if ((a & 1) or (b & 1)) else 1
            else:
                answer += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return answer


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.minFlips(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, 6, 5, 3)
    do_test(1, 4, 2, 7, 1)
    do_test(2, 1, 2, 3, 0)

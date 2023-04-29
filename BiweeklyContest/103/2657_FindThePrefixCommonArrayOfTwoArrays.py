from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ai = {n: i for i, n in enumerate(A)}
        bi = {n: i for i, n in enumerate(B)}

        s = set()
        resp = []
        for i in range(len(A)):
            s.add(A[i])
            s.add(B[i])

            count = 0
            for n in s:
                if ai[n] <= i and bi[n] <= i:
                    count += 1
            resp.append(count)

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findThePrefixCommonArray(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 2, 4], [3, 1, 2, 4], [0, 2, 3, 4])
    do_test(1, [2, 3, 1], [3, 1, 2], [0, 1, 3])

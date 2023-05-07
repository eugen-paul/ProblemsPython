from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        A = [True] * n
        A[0] = False
        A[1] = False

        for i in range(2, math.floor(math.sqrt(n))+1):
            if A[i]:
                j = i*i
                while j < n:
                    A[j] = False
                    j += i

        return A.count(True)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.countPrimes(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 10, 4)
    do_test(1, 0, 0)
    do_test(2, 1, 0)
    do_test(3, 100, 25)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        i = 0
        while True:
            if len(v1) <= i and len(v2) <= i:
                return 0
            subv1 = int(v1[i]) if i < len(v1) else 0
            subv2 = int(v2[i]) if i < len(v2) else 0

            if subv1 < subv2:
                return -1
            if subv1 > subv2:
                return 1

            i += 1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.compareVersion(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "1.01", "1.001", 0)
    do_test(1, "1.0", "1.0.0", 0)
    do_test(2, "0.1", "1.1", -1)
    do_test(3, "0.0.0.0", "0", 0)
    do_test(4, "1.2.1.2", "1.2.1.2", 0)
    do_test(5, "1.2.1.2", "1.02.01.02", 0)
    do_test(6, "1.2.1.002", "1.2.1.3", -1)
    do_test(6, "1.2.1.004", "1.2.1.3", 1)

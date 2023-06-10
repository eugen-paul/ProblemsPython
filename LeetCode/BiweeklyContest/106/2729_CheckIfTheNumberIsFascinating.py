from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def isFascinating(self, n: int) -> bool:
        r = str(n)+str(n*2)+str(n*3)
        c = Counter(r)

        if "0" in c or len(c) != 9:
            return False

        return all([x == 1 for x in c.values()])

    def isFascinating_1(self, n: int) -> bool:
        s = str(n)

        r = s+str(n*2)+str(n*3)

        c = Counter(r)

        if "0" in c:
            return False
        if len(c) != 9:
            return False

        for k, v in c.items():
            if v != 1:
                return False
        return True


def do_test(i: int, s, r):
    c = Solution()
    resp = c.isFascinating(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 192, True)
    do_test(1, 100, False)
    do_test(2, 783, False)

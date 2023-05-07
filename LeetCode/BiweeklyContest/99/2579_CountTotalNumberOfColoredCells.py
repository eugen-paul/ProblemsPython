from collections import defaultdict
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def coloredCells(self, n: int) -> int:
        s = (n*(n+1)) // 2
        resp = s * 4 - n * 4 + 1
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.coloredCells(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 1, 1)
    do_test(1, 2, 5)
    do_test(2, 3, 13)

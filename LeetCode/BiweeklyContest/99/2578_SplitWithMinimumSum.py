from collections import defaultdict
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def splitNum(self, num: int) -> int:
        l = list(str(num))
        l.sort()
        a = "0"
        b = "0"
        for i, n in enumerate(l):
            if i % 2 == 1:
                a += n
            else:
                b += n
        return int(a)+int(b)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.splitNum(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4325, 59)
    do_test(1, 687, 75)
    do_test(2, 10, 1)

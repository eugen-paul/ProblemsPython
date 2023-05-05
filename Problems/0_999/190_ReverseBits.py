from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def reverseBits(self, n: int) -> int:
        s = f'{n:032b}'
        s = "".join(reversed(s))
        return int(s, 2)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.reverseBits(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 43261596, 964176192)
    do_test(1, 4294967293, 3221225471)

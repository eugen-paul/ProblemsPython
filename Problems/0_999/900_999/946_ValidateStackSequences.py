from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []

        while len(pushed) != 0 or len(popped) != 0:
            if len(popped) > 0 and len(s) > 0 and s[-1] == popped[0]:
                s.pop()
                popped.pop(0)
            elif len(pushed) > 0:
                s.append(pushed.pop(0))
            else:
                break

        return len(s) == 0 and len(popped) == 0 and len(pushed) == 0


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.validateStackSequences(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True)
    do_test(1, [1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False)
    do_test(2, [2], [2], True)
    do_test(3, [1, 2], [2, 1], True)
    do_test(4, [1, 2], [1, 2], False)

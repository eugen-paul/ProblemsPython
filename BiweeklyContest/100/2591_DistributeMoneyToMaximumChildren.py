from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        # Everyone must receive at least 1 dollar.
        money -= children
        count = 0
        for _ in range(children - 1):
            if money < 7:
                break
            money -= 7
            count += 1

        if money == 7:
            count += 1
        elif money == 3 and count == children - 1:
            count -= 1

        return count

    def distMoney_1(self, money: int, children: int) -> int:
        if money < children:
            return -1

        money -= children
        count = 0

        while money >= 7 and count <= children-1:
            count += 1
            money -= 7

        if money != 0 and count >= children:
            count = children-1
        elif money == 3 and count == children - 1:
            count -= 1

        return count


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.distMoney(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 20, 3, 1)
    do_test(1, 16, 2, 2)
    do_test(2, 8, 1, 1)
    do_test(3, 9, 1, 0)
    do_test(4, 9, 2, 1)
    do_test(6, 10, 2, 1)
    do_test(7, 5, 2, 0)
    do_test(8, 13, 3, 1)
    do_test(9, 17, 2, 1)
    do_test(10, 19, 2, 1)
    do_test(11, 4, 1, -1)

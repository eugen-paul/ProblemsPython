from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        if len(prices) == 1:
            return money
        prices.sort()
        a = prices[0] + prices[1]
        if money - a >= 0:
            return money - a
        return money


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.buyChoco(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 2], 3, 0)

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def comp(p: int) -> int:
            if p == len(prices):
                return 0

            resp = comp(p+1)

            buy = prices[p]
            for i in range(p+1, len(prices)):
                sell = prices[i]
                if sell - buy - fee > 0:
                    resp = max(resp, sell - buy-fee+comp(i+1))
                if i < len(prices)-1:
                    if prices[i+1] + fee < sell:
                        break
            return resp

        return comp(0)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxProfit(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 2, 8, 4, 9], 2, 8)
    do_test(1, [1, 3, 7, 5, 10, 3], 3, 6)

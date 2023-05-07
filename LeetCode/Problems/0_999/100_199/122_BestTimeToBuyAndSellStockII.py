from typing import List, Dict, Tuple, Counter


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_cost = prices[0]
        last = prices[0]
        resp = 0
        for n in prices:
            if last > n:
                resp += last-buy_cost
                buy_cost = n
            last = n
        resp += last-buy_cost

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxProfit(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [7, 1, 5, 3, 6, 4], 7)
    do_test(1, [1, 2, 3, 4, 5], 4)
    do_test(2, [7, 6, 4, 3, 1], 0)

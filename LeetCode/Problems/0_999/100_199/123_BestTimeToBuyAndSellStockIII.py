from typing import Deque, List, Dict, Tuple, Counter


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        part1 = Deque()

        best = 0
        cur = prices[0]
        for n in prices:
            cur = min(cur, n)
            best = max(best, n-cur)
            part1.append(best)
        part1.append(0)

        part2 = Deque()
        max_cost = prices[-1]
        for n in reversed(prices):
            max_cost = max(max_cost, n)
            part2.appendleft(max_cost - n)
        part1.appendleft(0)

        return max([a+b for a, b in zip(part1, part2)])


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxProfit(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 3, 5, 0, 0, 3, 1, 4], 6)
    do_test(1, [1, 2, 3, 4, 5], 4)
    do_test(2, [7, 6, 4, 3, 1], 0)

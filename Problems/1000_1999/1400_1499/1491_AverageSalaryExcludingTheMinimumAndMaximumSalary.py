from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary)-min(salary)-max(salary)) / (len(salary)-2)

    def average_1(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / (len(salary)-2)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.average(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [4000, 3000, 1000, 2000], 2500.0)
    do_test(1, [1000, 2000, 3000], 2000.0)

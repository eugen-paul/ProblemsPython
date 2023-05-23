import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


class KthLargest:
    nums: List[int]
    k: int

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self.k]


def do_test(i: int, s, n, r):
    el: KthLargest
    for i, c in enumerate(s):
        if c == "KthLargest":
            el = KthLargest(n[i][0], n[i][1])
        else:
            resp = el.add(n[i][0])
            if resp != r[i]:
                print("NOK")


if __name__ == "__main__":
    do_test(0,
            ["KthLargest", "add", "add", "add", "add", "add"],
            [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            [None, 4, 5, 5, 8, 8]
            )

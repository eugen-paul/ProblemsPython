import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class MedianFinder:
    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.values, num)

    def findMedian(self) -> float:
        if len(self.values) % 2 == 1:
            return self.values[len(self.values) // 2]
        else:
            return (self.values[len(self.values) // 2] + self.values[len(self.values) // 2 - 1]) / 2


def do_test(nr: int, s, n, r):
    o: MedianFinder
    for i, c in enumerate(s):
        if c == "MedianFinder":
            o = MedianFinder()
        elif c == "addNum":
            o.addNum(n[i][0])
        elif c == "findMedian":
            resp = o.findMedian()
            if r[i] != resp:
                print("Error", nr, "Response=", resp, "Expected=", r[i])


if __name__ == "__main__":
    do_test(0,
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [1], [2], [], [3], []],
            [None, None, None, 1.5, None, 2.0]
            )

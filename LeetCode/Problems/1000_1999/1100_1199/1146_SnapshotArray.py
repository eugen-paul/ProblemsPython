import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class SnapshotArray:

    a: List[List[Tuple[int, int]]]
    r: int

    def __init__(self, length: int):
        self.a = [[(0, 0)] for _ in range(length)]
        self.r = 0

    def set(self, index: int, val: int) -> None:
        if self.a[index][-1][0] == self.r:
            self.a[index][-1] = (self.r, val)
        else:
            self.a[index].append((self.r, val))

    def snap(self) -> int:
        self.r += 1
        return self.r-1

    def get(self, index: int, snap_id: int) -> int:

        def bs_a(a: List[Tuple[int, int]], v: int):
            l, r = 0, len(a)-1
            while l <= r:
                m = (r+l) // 2
                if v >= a[m][0]:
                    l = m + 1
                else:
                    r = m - 1
            return l-1

        bisect.bisect_right()

        sub = self.a[index]

        return self.a[index][bs_a(sub, snap_id)][1]


def do_test(i: int, s, n, r):
    o: SnapshotArray
    for c, d, v in zip(s, n, r):
        if c == "SnapshotArray":
            o = SnapshotArray(d[0])
        elif c == "set":
            o.set(d[0], d[1])
        elif c == "snap":
            o.snap()
        elif c == "get":
            resp = o.get(d[0], d[1])
            if resp != v:
                print(i, "error")


if __name__ == "__main__":
    do_test(0,
            ["SnapshotArray", "set", "snap", "set", "get"],
            [[3], [0, 5], [], [0, 6], [0, 0]],
            [None, None, 0, None, 5])

    do_test(1,
            ["SnapshotArray", "set", "snap",  "set", "snap",  "set",  "get",  "get",  "get"],
            [[3],             [0, 5],    [], [0, 6],     [], [0, 7], [0, 0], [0, 1], [0, 2]],
            [None,              None,     0,   None,      1,   None,      5,      6,      7])

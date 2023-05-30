import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class MyHashSet:
    def __init__(self):
        self.s = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            bisect.insort(self.s, key)

    def remove(self, key: int) -> None:
        pos = bisect.bisect_right(self.s, key)
        if pos > 0 and self.s[pos-1] == key:
            self.s.pop(pos-1)

    def contains(self, key: int) -> bool:
        pos = bisect.bisect_right(self.s, key)
        return pos > 0 and self.s[pos-1] == key


class MyHashSet_s:
    def __init__(self):
        self.s = set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        self.s.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.s


def do_test(t: int, s, n, r):
    o: MyHashSet
    for i, c in enumerate(s):
        if c == "MyHashSet":
            o = MyHashSet()
        elif c == "add":
            o.add(n[i][0])
        elif c == "contains":
            if (o.contains(n[i][0]) != r[i]):
                print(t, "Error on", i)
        else:
            o.remove(n[i][0])


if __name__ == "__main__":
    do_test(0,
            ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"],
            [[], [1], [2], [1], [3], [2], [2], [2], [2]],
            [None, None, None, True, False, None, True, None, False]
            )
    do_test(1,
            ["MyHashSet", "add", "contains", "remove", "contains"],
            [[],  [1],  [1],   [1],   [1]],
            [None, None, True, None, False]
            )
    do_test(2,
            ["MyHashSet", "add", "contains", "add", "contains", "remove", "contains", "contains"],
            [[],  [1],  [1],   [2],  [2],   [2],   [2],   [1]],
            [None, None, True, None, True, None, False, True]
            )
    do_test(2,
            ["MyHashSet", "add", "contains", "add", "contains", "remove"],
            [[],  [1],  [1],   [2],  [2],   [1]],
            [None, None, True, None, True, None]
            )

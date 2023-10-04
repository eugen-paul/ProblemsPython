from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class MyHashMap:

    def __init__(self):
        self.m = [-1] * (10**6+1)

    def put(self, key: int, value: int) -> None:
        self.m[key] = value

    def get(self, key: int) -> int:
        return self.m[key]

    def remove(self, key: int) -> None:
        self.m[key] = -1


def do_test(t: int, s, n, r):
    o = None
    for i, c in enumerate(s):
        if c == "MyHashMap":
            o = MyHashMap()
        elif c == "put":
            o.put(n[i][0], n[i][1])
        elif c == "get":
            a = o.get(n[i][0])
            if a != r[i]:
                print("NOK", i, "expected", r[i], "response", a)
        elif c == "remove":
            o.remove(n[i][0])


if __name__ == "__main__":
    do_test(0, ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
            [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]],
            [None, None, None, 1, -1, None, 1, None, -1])


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

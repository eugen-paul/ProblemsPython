from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b = big
        self.m = medium
        self.s = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.b -= 1
            return self.b >= 0
        elif carType == 2:
            self.m -= 1
            return self.m >= 0
        else:
            self.s -= 1
            return self.s >= 0


def do_test(t: int, s, n, r):
    o: ParkingSystem
    for i, c in enumerate(s):
        if c == "ParkingSystem":
            o = ParkingSystem(n[i][0], n[i][1], n[i][2])
        elif c == "addCar":
            resp = o.addCar(n[i][0])
            if resp != r[i]:
                print("Error on i = ", i)


if __name__ == "__main__":
    do_test(0,
            ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"],
            [[1, 1, 0], [1], [2], [3], [1]],
            [None, True, True, False, False]
            )

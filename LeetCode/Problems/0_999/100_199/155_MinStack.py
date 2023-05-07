from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class MinStack:

    st: Deque[int]
    mins: Deque[int]
    lastmin: int

    def __init__(self):
        self.st = Deque()
        self.mins = Deque()
        self.lastmin = inf

    def push(self, val: int) -> None:
        self.st.append(val)
        self.mins.append(self.lastmin)
        self.lastmin = min(self.lastmin, val)

    def pop(self) -> None:
        self.st.pop()
        self.lastmin = self.mins.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.lastmin


def do_test(i: int, s, n, r):
    c = MinStack()

    isError = False
    for j, command in enumerate(s):
        if command == "MinStack":
            c = MinStack()
        elif command == "push":
            c.push(n[j][0])
        elif command == "getMin":
            if c.getMin() != r[j]:
                print("NOK! Expected", r[j], "return", c.getMin())
                isError = True
        elif command == "pop":
            c.pop()
        elif command == "top":
            if c.top() != r[j]:
                print("NOK! Expected", r[j], "return", c.getMin())
                isError = True
        else:
            print("ERROR")

    if isError:
        print("ERROR", i)
    else:
        print("OK", i)


if __name__ == "__main__":
    do_test(0, ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
            [None, None, None, None, -3, None, 0, -2]
            )

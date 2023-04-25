import bisect
from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class SmallestInfiniteSet:

    removed: List[Tuple[int, int]]

    def __init__(self):
        self.removed = []

    def popSmallest(self) -> int:
        if len(self.removed) == 0:
            self.removed.append((1, 1))
            return 1

        if self.removed[0][0] == 1:
            resp = self.removed[0][1]+1
            self.removed[0] = (self.removed[0][0], resp)
            if len(self.removed) > 1 and self.removed[1][0] == resp + 1:
                self.removed[0:2] = [(self.removed[0][0], self.removed[1][1])]
            return resp
        if self.removed[0][0] == 2:
            self.removed[0] = (1, self.removed[0][1])
        else:
            self.removed.insert(0, (1, 1))
        return 1

    def addBack(self, num: int) -> None:
        if len(self.removed) == 0 or self.removed[0][0] > num or self.removed[-1][1] < num:
            return

        pos = bisect.bisect_left(self.removed, (num, 0))
        if pos == len(self.removed) or self.removed[pos][0] != num:
            pos -= 1

        if self.removed[pos][0] == num and self.removed[pos][1] == num:
            self.removed.pop(pos)
        elif self.removed[pos][0] == num:
            self.removed[pos] = (self.removed[pos][0] + 1, self.removed[pos][1])
        elif self.removed[pos][1] == num:
            self.removed[pos] = (self.removed[pos][0], self.removed[pos][1] - 1)
        elif self.removed[pos][1] > num:
            self.removed[pos:pos+1] = [(self.removed[pos][0], num-1), (num+1, self.removed[pos][1])]


class SmallestInfiniteSet_i:
    """sample Solution"""

    def __init__(self):
        self.is_present: Set[int] = set()
        self.added_integers: List[int] = []
        self.current_integer = 1

    def popSmallest(self) -> int:
        # If there are numbers in the min-heap,
        # top element is lowest among all the available numbers.
        if len(self.added_integers):
            answer = heapq.heappop(self.added_integers)
            self.is_present.remove(answer)
        # Otherwise, the smallest number of large positive set
        # denoted by 'current_integer' is the answer.
        else:
            answer = self.current_integer
            self.current_integer += 1
        return answer

    def addBack(self, num: int) -> None:
        if self.current_integer <= num or num in self.is_present:
            return
        # We push 'num' in the min-heap if it isn't already present.
        heapq.heappush(self.added_integers, num)
        self.is_present.add(num)


def do_test(i: int, s, n, r):
    ob: SmallestInfiniteSet
    for j, c in enumerate(s):
        if c == "SmallestInfiniteSet":
            ob = SmallestInfiniteSet()
        elif c == "addBack":
            ob.addBack(n[j][0])
        elif c == "popSmallest":
            resp = ob.popSmallest()
            if resp != r[j]:
                print("Error", r[j], resp)


if __name__ == "__main__":
    do_test(0,
            ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest",
                "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"],
            [[], [2], [], [], [], [1], [], [], []],
            [None, None, 1, 2, 3, None, 1, 4, 5]
            )
    do_test(1,
            ["SmallestInfiniteSet", "popSmallest", "popSmallest", "addBack", "popSmallest", "addBack", "popSmallest", "popSmallest"],
            [[], [], [], [3], [], [2], [], []],
            [None, 1, 2, None, 3, None, 2, 4]
            )

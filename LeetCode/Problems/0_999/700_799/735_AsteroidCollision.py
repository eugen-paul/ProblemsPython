from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = Deque()
        resp = []

        for n in asteroids:
            if n < 0:
                if len(q) == 0:
                    resp.append(n)
                else:
                    explode = False
                    while not explode and q:
                        a = q[-1]
                        if a > -n:
                            explode = True
                        elif a == -n:
                            explode = True
                            q.pop()
                        else:
                            q.pop()
                    if not explode:
                        resp.append(n)
            else:
                q.append(n)

        resp.extend(q)
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.asteroidCollision(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [5, 10, -5], [5, 10])
    do_test(1, [8, -8], [])
    do_test(2, [10, 2, -5], [10])

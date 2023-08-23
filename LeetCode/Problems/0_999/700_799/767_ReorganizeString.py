from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:

    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        cnt = Counter(s)
        resp = []
        last = "-"
        while cnt:
            most = cnt.most_common(2)
            if len(most) == 1 and last == most[0][0]:
                return ""
            if last == most[0][0]:
                resp.append(most[1][0])
                if most[1][1] == 1:
                    del cnt[most[1][0]]
                else:
                    cnt[most[1][0]] -= 1
                last = most[1][0]
            else:
                resp.append(most[0][0])
                if most[0][1] == 1:
                    del cnt[most[0][0]]
                else:
                    cnt[most[0][0]] -= 1
                last = most[0][0]

        return "".join(resp)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.reorganizeString(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "aab", "aba")
    do_test(1, "aaab", "")
    do_test(2, "abc", "abc")
    do_test(3, "aaa", "")
    do_test(4, "a", "a")
    do_test(5, "aabbcc", "abcabc")
    do_test(6, "vvvlo", "vlvov")


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

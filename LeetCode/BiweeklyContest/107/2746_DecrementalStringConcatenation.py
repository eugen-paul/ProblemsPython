from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        m: Dict[Tuple[str, str], int] = dict()
        m[(words[0][0], words[0][-1])] = len(words[0])

        for i in range(1, len(words)):
            w = words[i]
            s, e = w[0], w[-1]
            tmp: Dict[Tuple[str, str], int] = dict()
            for k, v in m.items():
                if e == k[0]:
                    tmp[(s, k[-1])] = min(tmp.get((s, k[-1]), inf), v+len(w)-1)
                else:
                    tmp[(s, k[-1])] = min(tmp.get((s, k[-1]), inf), v+len(w))

                if k[-1] == s:
                    tmp[(k[0], e)] = min(tmp.get((k[0], e), inf), v+len(w)-1)
                else:
                    tmp[(k[0], e)] = min(tmp.get((k[0], e), inf), v+len(w))
            m = tmp

        return min(m.values())


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minimizeConcatenatedLength(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["aa", "ab", "bc"], 4)
    do_test(1, ["ab", "b"], 2)
    do_test(2, ["aaa", "c", "aba"], 6)
    do_test(3, ["a", "b", "c"], 3)
    do_test(4, ["ab", "ab", "ab", "bbbb"], 9)
    do_test(5, ["ab"], 2)
    do_test(6, ["abc", "cb", "c"], 5)
    do_test(7, ["aaa", "bba", "bb"], 6)


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

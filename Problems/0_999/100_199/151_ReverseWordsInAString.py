from collections import defaultdict
from functools import cache
from math import inf
import re
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def reverseWords(self, s: str) -> str:
        resp = []
        w = []
        for c in s:
            if c != " ":
                w += [c]
            elif len(w) > 0:
                resp.append(" ")
                resp.extend(reversed(w))
                w.clear()
        if len(w) > 0:
            resp.append(" ")
            resp.extend(reversed(w))

        return "".join(reversed(resp[1:]))

    def reverseWords_3(self, s: str) -> str:
        return " ".join(reversed(s.strip().split()))

    def reverseWords_2(self, s: str) -> str:
        s = re.sub(r"\s+", " ", s)
        s = s.strip().split(" ")
        return " ".join(w for w in reversed(s))

    def reverseWords_1(self, s: str) -> str:
        s = s.strip().split(" ")
        resp = ""
        for w in reversed(s):
            if len(w) > 0:
                resp += " " + w
        return resp[1:]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.reverseWords(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "the sky is blue", "blue is sky the")
    do_test(1, "  hello world  ", "world hello")
    do_test(2, "a good   example", "example good a")

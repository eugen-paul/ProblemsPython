from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dictionary = set(dictionary)

        @cache
        def do(pos: int) -> int:
            if pos >= len(s):
                return 0

            best = len(s) - pos
            for i in range(pos+1, len(s)+1):
                a = s[pos:i]
                if a in dictionary:
                    best = min(best, do(i))

            best = min(best, do(pos+1) + 1)

            return best

        return do(0)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minExtraChar(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "leetscode",  ["leet", "code", "leetcode"], 1)
    do_test(1, "sayhelloworld",  ["hello", "world"], 3)

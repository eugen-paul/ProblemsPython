from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        resp = []

        def check(sub: str, sl: List[str]) -> None:
            if len(sub) == 0:
                resp.append(" ".join(sl))
                return

            for w in wordDict:
                if sub.startswith(w):
                    check(sub[len(w):], sl + [w])

        check(s, [])
        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.wordBreak(s, n)
    r.sort()
    resp.sort()
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "catsanddog", ["cat", "cats", "and", "sand", "dog"], ["cats and dog", "cat sand dog"])
    do_test(1, "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    do_test(2, "catsandog", ["cats", "dog", "sand", "and", "cat"], [])

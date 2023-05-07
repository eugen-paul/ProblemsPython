from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m: List[bool] = [False] * (len(s)+1)

        def check(sub: str) -> bool:
            if len(sub) == 0:
                return True
            if m[len(sub)]:
                return False
            m[len(sub)] = True

            for w in wordDict:
                if sub.startswith(w) and check(sub[len(w):]):
                    return True
            return False

        return check(s)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.wordBreak(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "leetcode", ["leet", "code"], True)
    do_test(1, "applepenapple", ["apple", "pen"], True)
    do_test(2, "catsandog", ["cats", "dog", "sand", "and", "cat"], False)

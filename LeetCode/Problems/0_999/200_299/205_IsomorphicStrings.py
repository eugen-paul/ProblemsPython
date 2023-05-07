from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = [" "] * 128

        for i, c in enumerate(s):
            so = ord(c)
            if m[so] == " ":
                m[so] = t[i]
            elif m[so] != t[i]:
                return False
        m = [c for c in m if c != " "]
        cnt = Counter(m)
        return cnt.most_common(1)[0][1] == 1

    def isIsomorphic_i(self, s: str, t: str) -> bool:
        """sample solution"""
        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):
            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.isIsomorphic(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "egg", "add", True)
    do_test(1, "foo", "bar", False)
    do_test(2, "badc", "baba", False)

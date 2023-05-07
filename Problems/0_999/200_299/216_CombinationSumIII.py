from collections import defaultdict
from functools import cache
import itertools
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        resp = []

        def comp(f: int, k: int, n: int, cur: Deque[int]):
            if k <= 0:
                return

            for i in range(f, 10):
                rest = n-i
                if rest < 0:
                    return
                cur.append(i)
                if rest == 0 and k == 1:
                    resp.append(list(cur))
                comp(i+1, k-1, rest, cur)
                cur.pop()

        comp(1, k, n, Deque())

        return resp

    def combinationSum3_i(self, k: int, n: int) -> List[List[int]]:
        """internet solution:
        https://leetcode.com/problems/combination-sum-iii/solutions/2027170/python3-3-lines-of-code/
        """
        nums = [i for i in range(1, 10)]
        comb = itertools.combinations(nums, k)
        return [c for c in comb if sum(c) == n]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.combinationSum3(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 7, [[1, 2, 4]])

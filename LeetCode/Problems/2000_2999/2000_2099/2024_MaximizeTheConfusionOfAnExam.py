from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def comp(v: str) -> int:
            l, resp, cnt = 0, 0, 0
            for r in range(len(answerKey)):
                cnt += 1 if answerKey[r] != v else 0
                while cnt > k:
                    cnt -= 1 if answerKey[l] != v else 0
                    l += 1
                resp = max(r-l+1, resp)
            return resp

        return max(comp("T"), comp("F"))


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxConsecutiveAnswers(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "TTFF", 2, 4)
    do_test(1, "TFFT", 1, 3)
    do_test(2, "TTFTTFTT", 1, 5)

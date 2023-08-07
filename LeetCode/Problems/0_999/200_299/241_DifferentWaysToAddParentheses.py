from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import re

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def solve(start, end) -> List[int]:
            pos = start
            resp = []
            n = re.search(r'\d+', expression[pos:end])[0]
            if len(n) == end - pos:
                resp.append(int(n))
                return resp

            while True:
                op = expression[pos+len(n)]

                left = solve(start, pos+len(n))
                right = solve(pos+len(n)+1, end)

                for l in left:
                    for r in right:
                        if op == "-":
                            resp += [l-r]
                        elif op == "+":
                            resp += [l+r]
                        else:
                            resp += [l*r]
                pos += len(n)+1
                n = re.search(r'\d+', expression[pos:end])[0]
                if len(n) == end - pos:
                    break
            return resp

        return solve(0, len(expression))


def do_test(i: int, s, r):
    c = Solution()
    resp = c.diffWaysToCompute(s)
    resp.sort()
    r.sort()
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "2-1-1", [0, 2])
    do_test(1, "2*3-4*5", [-34, -14, -10, -10, 10])

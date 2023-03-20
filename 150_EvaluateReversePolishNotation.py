from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "-", "/", "*"}
        st = Deque()

        for n in tokens:
            if n not in op:
                st.append(int(n))
            else:
                b = st.pop()
                a = st.pop()
                if n == "+":
                    st.append(a+b)
                elif n == "-":
                    st.append(a-b)
                elif n == "/":
                    if a / b >= 0:
                        st.append(a//b)
                    else:
                        st.append(math.ceil(a/b))
                elif n == "*":
                    st.append(a*b)

        return st[0]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.evalRPN(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["2", "1", "+", "3", "*"], 9)
    do_test(1, ["4", "13", "5", "/", "+"], 6)
    do_test(2, ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)

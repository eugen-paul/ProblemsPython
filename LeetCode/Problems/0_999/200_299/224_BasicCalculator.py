from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

import sys
sys.setrecursionlimit(10000)


class Solution:
    def calculate_2(self, s: str) -> int:
        """internet solution
        https://leetcode.com/problems/basic-calculator/solutions/3227625/224-time-93-3-solution-with-step-by-step-explanation/
        """
        ans = 0
        num = 0
        sign = 1
        stack = [sign]  # stack[-1]: current env's sign

        for c in s:
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0'))
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            elif c == '+' or c == '-':
                ans += sign * num
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0

        return ans + sign * num

    def calculate_i(self, s: str) -> int:
        """internet solution
        https://leetcode.com/problems/basic-calculator/solutions/2834479/python3-o-n-stack-solution/
        """
        val_stack = []
        cur_num = 0
        total = 0
        sign = 1
        for c in s:
            if c.isdigit():
                cur_num *= 10
                cur_num += int(c)
            elif c == '+':
                total += cur_num*sign
                cur_num = 0
                sign = 1
            elif c == '-':
                total += cur_num*sign
                cur_num = 0
                sign = -1
            elif c == '(':
                val_stack.append(total)
                val_stack.append(sign)
                sign = 1
                total = 0
            elif c == ')':
                total += sign * cur_num
                cur_num = 0
                total *= val_stack.pop()
                total += val_stack.pop()
        if cur_num:
            total += sign * cur_num
        return total

    def calculate(self, s: str) -> int:
        s = s.strip().replace(" ", "")

        def read_next_value(sub: str) -> Tuple[int, str]:
            v = ""
            for n in sub:
                if (n == "-" and len(v) == 0) or n not in "+-()":
                    v += n
                else:
                    break

            if len(v) != 0 and v != "-":
                return (int(v), sub[len(v):])

            c = 0
            l = 0
            for n in sub:
                l += 1
                if n == "(":
                    c += 1
                elif n == ")":
                    c -= 1
                    if c == 0:
                        break

            if v == "-":
                return (-self.calculate(sub[2:l-1]), sub[l:])
            else:
                return (self.calculate(sub[1:l-1]), sub[l:])

        last, s = read_next_value(s)

        while s != "":
            exp = s[0]
            v2, s = read_next_value(s[1:])
            if exp == "+":
                last = last+v2
            if exp == "-":
                last = last-v2

        return last

    def calculate_1(self, s: str) -> int:
        return eval(s)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.calculate(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "1 + 1", 2)
    do_test(1, " 2-1 + 2 ", 3)
    do_test(2, "(1+(4+5+2)-3)+(6+8)", 23)
    do_test(3, "-1", -1)
    do_test(4, "2", 2)
    do_test(5, "2+(-1)", 1)
    do_test(6, "- (3 + (4 + 5))", -12)
    do_test(7, "- (1+1)", -2)
    do_test(8, "- (-1-1)", 2)

from typing import Dict, List, Set


class Solution:
    def add_brackets_one(self, m: Dict[int, Set[str]], s: Set[str], left: int):
        for x in m[left]:
            s.add("("+x+")")
            s.add("()"+x)
            s.add(x+"()")

    def add_brackets(self, m: Dict[int, Set[str]], s: Set[str], left: int, right: int):
        for x in m[left]:
            for x2 in m[right]:
                s.add(x+x2)
                if left != right:
                    s.add(x2+x)

    def generateParenthesis(self, n: int) -> List[str]:
        m = {
            1: {"()"},
            2: {"(())", "()()"},
        }

        if n == 1:
            return list(m[1])
        if n == 2:
            return list(m[2])

        for i in range(3, n+1):
            set_of_i = set()
            self.add_brackets_one(m, set_of_i, i-1)
            for j in range(2, (i // 2) + 1):
                self.add_brackets(m, set_of_i, j, i-j)
            m[i] = set_of_i

        return list(m[n])

    def generateParenthesis_2(self, n: int) -> List[str]:
        m = {
            1: {"()"},
            2: {"(())", "()()"},
        }

        if n == 1:
            return list(m[1])
        if n == 2:
            return list(m[2])

        if n >= 3:
            n3 = set()
            self.add_brackets_one(m, n3, 2)
            m[3] = n3

        if n >= 4:
            n4 = set()
            self.add_brackets_one(m, n4, 3)
            self.add_brackets(m, n4, 2, 2)
            m[4] = n4

        if n >= 5:
            n5 = set()
            self.add_brackets_one(m, n5, 4)
            self.add_brackets(m, n5, 2, 3)
            m[5] = n5

        if n >= 6:
            n6 = set()
            self.add_brackets_one(m, n6, 5)
            self.add_brackets(m, n6, 3, 3)
            self.add_brackets(m, n6, 2, 4)
            m[6] = n6

        if n >= 7:
            n7 = set()
            self.add_brackets_one(m, n7, 6)
            self.add_brackets(m, n7, 2, 5)
            self.add_brackets(m, n7, 3, 4)
            m[7] = n7

        if n >= 8:
            n8 = set()
            self.add_brackets_one(m, n8, 7)
            self.add_brackets(m, n8, 2, 6)
            self.add_brackets(m, n8, 3, 5)
            self.add_brackets(m, n8, 4, 4)
            m[8] = n8

        return list(m[n])

    def generateParenthesis_slow(self, n: int) -> List[str]:
        m = {
            1: {"()"},
            2: {"(())", "()()"},
        }

        if n == 1:
            return list(m[1])
        if n == 2:
            return list(m[2])

        if n >= 3:
            n3 = set()
            for x in m[2]:
                n3.add("("+x+")")
                n3.add("()"+x)
                n3.add(x+"()")
            m[3] = n3

        if n >= 4:
            n4 = set()
            for x in m[3]:
                n4.add("("+x+")")
                n4.add("()"+x)
                n4.add(x+"()")
            for x in m[2]:
                for x2 in m[2]:
                    n4.add(x+x2)
            m[4] = n4

        if n >= 5:
            n5 = set()
            for x in m[4]:
                n5.add("("+x+")")
                n5.add("()"+x)
                n5.add(x+"()")
            for x in m[2]:
                for x2 in m[3]:
                    n5.add(x+x2)
                    n5.add(x2+x)
            m[5] = n5

        if n >= 6:
            n6 = set()
            for x in m[5]:
                n6.add("("+x+")")
                n6.add("()"+x)
                n6.add(x+"()")
            for x in m[3]:
                for x2 in m[3]:
                    n6.add(x+x2)
                    n6.add(x2+x)
            for x in m[2]:
                for x2 in m[4]:
                    n6.add(x+x2)
                    n6.add(x2+x)
            m[6] = n6

        if n >= 7:
            n7 = set()
            for x in m[6]:
                n7.add("("+x+")")
                n7.add("()"+x)
                n7.add(x+"()")
            for x in m[3]:
                for x2 in m[4]:
                    n7.add(x+x2)
                    n7.add(x2+x)
            for x in m[2]:
                for x2 in m[5]:
                    n7.add(x+x2)
                    n7.add(x2+x)
            m[7] = n7

        if n >= 8:
            n8 = set()
            for x in m[7]:
                n8.add("("+x+")")
                n8.add("()"+x)
                n8.add(x+"()")
            for x in m[3]:
                for x2 in m[5]:
                    n8.add(x+x2)
                    n8.add(x2+x)
            for x in m[2]:
                for x2 in m[6]:
                    n8.add(x+x2)
                    n8.add(x2+x)
            for x in m[4]:
                for x2 in m[4]:
                    n8.add(x+x2)
                    n8.add(x2+x)
            m[8] = n8

        return list(m[n])


def do_test(i: int, s, r):
    c = Solution()
    resp = c.generateParenthesis(s)
    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", sorted(r), "response", sorted(resp))


if __name__ == "__main__":
    do_test(0, 3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
    do_test(1, 1, ["()"])
    do_test(2, 2, ["(())", "()()"])
    do_test(3, 4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
            "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])
    do_test(4, 5, ["((((()))))", "(((()())))", "(((())()))", "(((()))())", "(((())))()", "((()(())))", "((()()()))", "((()())())", "((()()))()", "((())(()))", "((())()())", "((())())()", "((()))(())", "((()))()()", "(()((())))", "(()(()()))", "(()(())())", "(()(()))()", "(()()(()))", "(()()()())", "(()()())()",
            "(()())(())", "(()())()()", "(())((()))", "(())(()())", "(())(())()", "(())()(())", "(())()()()", "()(((())))", "()((()()))", "()((())())", "()((()))()", "()(()(()))", "()(()()())", "()(()())()", "()(())(())", "()(())()()", "()()((()))", "()()(()())", "()()(())()", "()()()(())", "()()()()()"])

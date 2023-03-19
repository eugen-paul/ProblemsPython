class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = list()

        lvl = 0
        bst_lvl = 0
        for i, c in enumerate(s):
            if c == '(':
                lvl += 1
                if lvl > len(m):
                    m.append(i)
            else:
                if lvl >= 1:
                    curr_len = i-m[lvl-1] + 1
                    bst_lvl = max(bst_lvl, curr_len)
                    if lvl < len(m):
                        m.pop()
                    lvl -= 1
                else:
                    lvl = 0
                    m.clear()

        return bst_lvl

    def longestValidParentheses_web_solution(self, s: str) -> int:
        max_length = 0
        stck = [-1]  # position befor start of current window
        for i in range(len(s)):
            if s[i] == '(':
                stck.append(i)
            else:
                stck.pop()
                if not stck:  # Current window is no longer valid (lvl == -1). Start new window.
                    stck.append(i)
                else:
                    max_length = max(max_length, i-stck[-1])  # update the length of the valid substring
        return max_length

    def longestValidParentheses_fast_but_need_a_lot_of_memory(self, s: str) -> int:
        m = dict()

        lvl = 0
        bst_lvl = 0
        for i, c in enumerate(s):
            if c == '(':
                lvl += 1
                if lvl not in m:
                    m[lvl] = i
            else:
                if lvl >= 1:
                    curr_len = i-m[lvl] + 1
                    bst_lvl = max(bst_lvl, curr_len)
                    if (lvl+1) in m:
                        m.pop(lvl+1)
                    lvl -= 1
                else:
                    lvl = 0
                    m.clear()

        return bst_lvl


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestValidParentheses(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "(()", 2)
    do_test(1, ")()())", 4)
    do_test(2, "", 0)
    do_test(3, ")(", 0)
    do_test(4, "()", 2)
    do_test(5, "())))))", 2)
    do_test(6, "()()()", 6)
    do_test(7, "()(())()", 8)
    do_test(8, "((()))))))))))()()()()", 8)
    do_test(9, "((()))))))))))()()", 6)
    do_test(10, "((()))))))))", 6)
    do_test(11, "()()()(", 6)
    do_test(12, "((()))(()(", 6)

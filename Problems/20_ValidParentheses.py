class Solution:
    def isValid(self, s: str) -> bool:
        last_brackets = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                last_brackets.append(c)
                continue

            try:
                lb = last_brackets.pop()
            except IndexError:
                return False
            if (c == ')' and lb != '(') \
                    or (c == ']' and lb != '[') \
                    or (c == '}' and lb != '{'):
                return False

        return len(last_brackets) == 0

    def isValid_2(self, s: str) -> bool:
        last_brackets = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                last_brackets.append(c)
                continue
            if (len(last_brackets) == 0):
                return False

            lb = last_brackets.pop()
            if (c == ')' and lb != '(') \
                    or (c == ']' and lb != '[') \
                    or (c == '}' and lb != '{'):
                return False

        return len(last_brackets) == 0


def do_test(i: int, s, r):
    c = Solution()
    resp = c.isValid(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "()", True)
    do_test(1, "()[]{}", True)
    do_test(2, "(]", False)
    do_test(3, "]", False)
    do_test(4, "())", False)
    do_test(5, "(", False)
    do_test(6, "({)}", False)

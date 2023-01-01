import re


class Solution:
    def isMatchRegex(self, s: str, p: str) -> bool:
        x = re.search("^"+p+"$", s)
        return x is not None and (x.group(0) == s)

    def isMatch(self, s: str, p: str) -> bool:
        # end of text and of RegEx was reached
        if len(p) == 0 and len(s) == 0:
            return True

        # End of RegEx but not of text was reached
        if len(p) == 0:
            return False

        match_char = ""
        match_any = False
        match_many = False

        # get next RegEx char
        match_char = p[0]
        match_any = (match_char == '.')
        match_many = False
        if len(p) >= 2 and p[1] == '*':
            match_many = True

        # check if next RegEx char repeats itself
        delta = 2
        while match_many and len(p) > delta + 2 and match_char == p[delta] and p[delta+1] == "*":
            delta += 2

        # End of text but not of RegEx was reached
        if len(s) == 0 and match_many:
            return self.isMatch(s[1:], p[2:])
        if len(s) == 0 and not match_many:
            # next char of RegEx must be present, but there is none
            return False

        # get next text char
        current_char = s[0] if len(s) > 0 else None

        # current character must be present
        if not match_many:
            if not match_any:
                # current character is a specific character and must be present
                if match_char != current_char:
                    return False
            # current character match and must be present
            return self.isMatch(s[1:], p[1:])

        if not match_any:
            # current character is a specific character and can be present
            if match_char != current_char:
                # current character is a specific character and don'n match
                # check next RegEx char
                return self.isMatch(s, p[delta:])

        # current character is a specific character and match
        # check :
        #  - current char with next RegEx char
        #  - next char with next RegEx char
        #  - next char with current RegEx char
        return self.isMatch(s, p[delta:]) \
            or self.isMatch(s[1:], p[delta:]) \
            or self.isMatch(s[1:], p)


def do_test(i: int, s: str, p: str, r):
    c = Solution()
    resp = c.isMatchRegex(s, p)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


def do_test_long(i: int, s: str, p: str, r):
    c = Solution()
    resp = c.isMatchRegex(s, p)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(-1, "aa", "..", True)
    do_test(0, "aa", "a", False)
    do_test(1, "aa", "a*", True)
    do_test(2, "ab", ".*", True)
    do_test(3, "aaaaa", "a*", True)
    do_test(4, "aaaaa", "a*ba", False)
    do_test(5, "aabaa", "a*ba", False)
    do_test(6, "aaaba", "a*ba", True)
    do_test(7, "aaa", "a*b*a*", True)
    do_test(8, "aaTa", "a*T*a*", True)
    do_test(9, "aaTa", "a*.*T*a*", True)
    do_test(9, "aaQTERTa", "a*.*T*a*", True)
    do_test(10, "mississippi", "mis*is*p*.", False)
    do_test(11, "a", "ab*", True)
    do_test(12, "ab", ".*c", False)
    do_test(13, "bbbba", ".*a*a", True)
    do_test(14, "a", ".*..a*", False)
    do_test(15, "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False)
    do_test(16, "aaaaaaaaaaaaac", "a*a*a*a*a*a*a*a*a*c", True)
    do_test_long(-1, "aa", "..", True)
    do_test_long(0, "aa", "a", False)
    do_test_long(1, "aa", "a*", True)
    do_test_long(2, "ab", ".*", True)
    do_test_long(3, "aaaaa", "a*", True)
    do_test_long(4, "aaaaa", "a*ba", False)
    do_test_long(5, "aabaa", "a*ba", False)
    do_test_long(6, "aaaba", "a*ba", True)
    do_test_long(7, "aaa", "a*b*a*", True)
    do_test_long(8, "aaTa", "a*T*a*", True)
    do_test_long(9, "aaTa", "a*.*T*a*", True)
    do_test_long(9, "aaQTERTa", "a*.*T*a*", True)
    do_test_long(10, "mississippi", "mis*is*p*.", False)
    do_test_long(11, "a", "ab*", True)
    do_test_long(12, "ab", ".*c", False)
    do_test_long(13, "bbbba", ".*a*a", True)
    do_test_long(14, "a", ".*..a*", False)
    do_test_long(15, "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False)
    do_test_long(16, "aaaaaaaaaaaaac", "a*a*a*a*a*a*a*a*a*c", True)

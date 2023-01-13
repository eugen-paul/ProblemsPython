import re


class Solution:
    def is_equal(self, a: str, b: str) -> bool:
        for i in range(len(a)):
            if a[i] == "?" or b[i] == "?":
                continue
            if a[i] != b[i]:
                return False

        return True

    def get_pos(self, s: str, p: str, offset: int) -> int:
        if len(s) - offset < len(p):
            return -1

        for i in range(offset, len(s) - len(p) + 1):
            a = s[i: i+len(p)]
            if self.is_equal(a, p):
                return i

        return -1

    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        while "**" in p:
            p = p.replace("**", "*")

        splits = p.split("*")

        if len(splits) == 1:
            return len(s) == len(p) and self.is_equal(s, p)

        first = splits[0]
        a = s[:len(first)]
        if len(first) > 0 and not self.is_equal(a, first):
            return False

        last = splits[-1]
        a = s[-len(last):]
        if len(last) > 0 and not self.is_equal(a, last):
            return False

        offset = 0
        for sp in splits:
            next_pos = self.get_pos(s, sp, offset)
            if next_pos == -1:
                return False
            offset = next_pos + len(sp)

        return True

    def isMatch_funny(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        origin_p = p

        while "**" in p:
            p = p.replace("**", "*")

        splits = p.replace("?", "*").split("*")

        offset = 0
        try:
            for sp in splits:
                pos_sp = s.index(sp, offset)
                offset = pos_sp + len(sp)
        except IndexError:
            return False
        except ValueError:
            return False

        if p[0] == "*" and p[-1] == "*" and "?" not in origin_p:
            return True

        if len(splits) > 1 and len(splits[0]) != 0 and s.startswith(splits[0]) and len(splits[-1]) != 0 and s.endswith(splits[-1]) and "?" not in origin_p:
            return True

        if len(splits[0]) != 0 and s.startswith(splits[0]) and p[-1] == "*" and "?" not in origin_p:
            return True

        if len(splits[-1]) != 0 and s.endswith(splits[-1]) and p[0] == "*" and "?" not in origin_p:
            return True

        if p[-1] != "*" and not s.endswith(splits[-1]) and "?" not in origin_p:
            return False

        if p[0] != "*" and not s.startswith(splits[0]) and "?" not in origin_p:
            return False

        r = re.compile(p.replace("*", ".*").replace("?", "."))
        return r.fullmatch(s) is not None


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.isMatch(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "aa", "a", False)
    do_test(1, "aa", "*", True)
    do_test(2, "cb", "?a", False)
    do_test(3, "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
            "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb", False)
    do_test(4, "abbbaaababbaaabaaabbbabbbbaaabbaaababaabbbbbbaababbabababbababaaabbbbbabababaababaaaaaaabbbaabaabbbaabbabaababbabaababbbabbaaabbbaaaababbaaabbaabaabbbbbaaababaabaabaaabbabaabbbabbbaabbababaabbbbbbbbaaa",
            "*ba***bba*b**abbaa***a*****b*a*bb*b***a*bbb***a***bba*****a****a*a*b**aaaba*aab*a*aa***a*a*b**b**a*b*", True)
    do_test(5, "baaabbabbbaabbbbbbabbbaaabbaabbbbbaaaabbbbbabaaaaabbabbaabaaababaabaaabaaaabbabbbaabbbbbaababbbabaaabaabaaabbbaababaaabaaabaaaabbabaabbbabababbbbabbaaababbabbaabbaabbbbabaaabbababbabababbaabaabbaaabbba",
            "*b*ab*bb***abba*a**ab***b*aaa*a*b****a*b*bb**b**ab*ba**bb*bb*baab****bab*bbb**a*a*aab*b****b**ba**abba", False)
    do_test(6, "aabaabbbabbaaabbbbaabbbbbabbbbaabbaaaababaababbbabbbababbbbabbaaabaabbaaaaaabbababbaababbbaaaaaabbaaaabaabbbabaaababbaaabaabbababbbabaabbbababbbababaabbbbbaaaababbbbababbbaaabbabaabababaabbbbbaaaaabaabaab",
            "a***aba**a*a****bb**bb*aa**baa*b*b***a*baa***a*aba**ba***a**a*a*aa**abaab**a*ab*b*b*aaa*aa*b**a***b*ab", True)
    do_test(7, "cb", "??", True)
    do_test(8, "cb", "*", True)
    do_test(9, "cb", "*a*", False)
    do_test(10, "cb", "*a*", False)
    do_test(11, "cb", "*c*", True)
    do_test(12, "cb", "*b*", True)
    do_test(13, "cb", "b*", False)
    do_test(14, "cb", "*c", False)
    do_test(15, "cb", "c*", True)
    do_test(16, "cb", "*b", True)

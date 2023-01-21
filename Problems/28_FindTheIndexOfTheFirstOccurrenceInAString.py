class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStr_2(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:].startswith(needle):
                return i

        return -1

    def strStr_1(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1

        for i in range(len(haystack) - len(needle) + 1):
            ok = True
            for j, c in enumerate(needle):
                if haystack[i+j] != c:
                    ok = False
                    break
            if ok:
                return i

        return -1


def do_test(i: int, s, t, r):
    c = Solution()
    resp = c.strStr(s, t)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "sadbutsad", "sad", 0)
    do_test(1, "leetcode", "leeto", -1)
    do_test(2, "aaab", "aab", 1)
    do_test(3, "test", "testi", -1)
    do_test(4, "testTesttest", "Test", 4)
    do_test(5, "test", "test", 0)

from typing import Counter, List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """some ideas from solution"""
        count_t = Counter(t)
        size_ct = len(count_t)

        l = 0
        r = 0

        resp = ""

        while r < len(s):
            if s[r] in count_t:
                count_t[s[r]] -= 1
                if count_t[s[r]] == 0:
                    size_ct -= 1

            while size_ct == 0:
                if len(resp) == 0 or len(resp) > r-l+1:
                    resp = s[l:r+1]

                if s[l] in count_t:
                    count_t[s[l]] += 1
                    if count_t[s[l]] == 1:
                        size_ct += 1
                l += 1

            r += 1

        return resp

    def minWindow_1(self, s: str, t: str) -> str:
        count_t = Counter(t)

        l = 0
        r = 0

        resp = ""
        count_s = Counter()

        while r < len(s):
            count_s[s[r]] += 1

            while count_s >= count_t:
                if len(resp) == 0 or len(resp) > r-l+1:
                    resp = s[l:r+1]
                count_s[s[l]] -= 1
                l += 1

            r += 1

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minWindow(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "ADOBECODEBANC", "ABC", "BANC")
    do_test(1, "a", "a", "a")
    do_test(2, "a", "aa", "")

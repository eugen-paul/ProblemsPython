from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        c = Counter(p)
        t = Counter(s[:len(p)])

        resp = []
        if c == t:
            resp.append(0)

        for i in range(len(s)-len(p)):
            t[s[i]] -= 1
            t[s[i + len(p)]] += 1
            if c == t:
                resp.append(i+1)

        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findAnagrams(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "cbaebabacd", "abc", [0, 6])
    do_test(1, "abab", "ab", [0, 1, 2])

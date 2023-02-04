from typing import Counter, List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])

        if c1 == c2:
            return True

        for i in range(len(s2) - len(s1)):
            c2[s2[i]] -= 1
            c2[s2[len(s1)+i]] += 1
            if c1 == c2:
                return True

        return False


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.checkInclusion(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "ab", "eidbaooo", True)
    do_test(1, "ab", "eidboaoo", False)

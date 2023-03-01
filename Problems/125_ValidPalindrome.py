from typing import List, Dict, Tuple, Counter


class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        for c in s:
            if 'a' <= c.lower() <= 'z' or '0' <= c.lower() <= '9':
                p += c.lower()
        return p == p[::-1]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.isPalindrome(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "A man, a plan, a canal: Panama", True)
    do_test(1, "race a car", False)
    do_test(2, " ", True)
    do_test(3, "3t", False)

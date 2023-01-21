class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


def do_test(i: int, s: int, r: bool):
    c = Solution()
    resp = c.isPalindrome(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 121, True)
    do_test(1, -42, False)
    do_test(2, 1, True)

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        """FAIL"""
        pass


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.isReachable(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 6, 9, False)
    do_test(1, 4, 7, True)

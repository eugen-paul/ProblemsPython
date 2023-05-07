class Solution:
    def climbStairs(self, n: int) -> int:
        pre_last = 0
        last = 1
        for _ in range(n):
            pre_last, last = last, last+pre_last
        return last


def do_test(i: int, s, r):
    c = Solution()
    resp = c.climbStairs(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, 2)
    do_test(1, 3, 3)
    do_test(2, 6, 13)

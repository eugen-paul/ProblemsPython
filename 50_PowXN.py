class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.myPow(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2.00000, 10, 1024.0)
    do_test(1, 2.1, 3, 9.261000000000001)
    do_test(2, 2.00000, -2, 0.25000)

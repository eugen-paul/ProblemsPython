from math import sqrt


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l = 1
        r = x // 2
        while l <= r:
            m = (l + r) // 2
            dop = m*m
            if dop == x:
                return m
            elif dop > x:
                r = m - 1
            else:
                l = m + 1

        return r

    def mySqrt_1(self, x: int) -> int:
        return int(sqrt(x))


def do_test(i: int, s, r):
    c = Solution()
    resp = c.mySqrt(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, 2)
    do_test(1, 8, 2)
    do_test(2, 1, 1)
    do_test(3, 0, 0)
    do_test(4, 15, 3)
    do_test(5, 16, 4)
    do_test(6, 17, 4)

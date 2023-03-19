class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        p = f"{abs(n):b}"
        r = 1
        for c in p:
            r *= r
            if c == "1":
                r *= x

        if n < 0:
            return 1 / r

        return r
    
    def myPow_bin(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        p = f"{abs(n):b}"
        r = x
        for i in range(1, len(p)):
            c = p[i]
            r *= r
            if c == "1":
                r *= x

        if n < 0:
            return 1 / r

        return r

    def myPow_simple(self, x: float, n: int) -> float:
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
    do_test(3, -2.00000, 2, 4)
    do_test(4, -2.00000, 3, -8)
    do_test(5, 0, 3, 0)
    do_test(6, 0, 0, 1)
    do_test(7, 4, 0, 1)

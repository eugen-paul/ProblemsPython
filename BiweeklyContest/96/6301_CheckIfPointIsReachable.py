import math


class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        """
        Rules:
           1. (x, y - x)
           2. (x - y, y)
           3. (2 * x, y)
           4. (x, 2 * y)
        A: If X is a power of base 2 and Y = 1, then you can reach the point (1,1).
            Example: (1,1)
                     (2,1)
                     (4,1)
        B: If X is a power of base 2 and Y = m, then you can reach the point (1,1).
            Example: x = 2 ** n, y = m
                    One comes to the point (1,m).
                    Then, by rule 1, you can move y to the next highest power of 2. y = p, where p = 2 ** h and m < p.
                    In the end, you move y to 1.
            Example: (1,123)
                     (2,21)
                     (4,412)
        C: From B follows that if X + n*Y is equal to 2 ** m, then the point is also reachable.
            Example: (1,2)    -> 1  + 0*2 = 1  = 2**0
                     (1,2)    -> 1  + 0*2 = 1  = 2**0
                     (10, 6)  -> 10 + 1*6 = 16 = 2**4
                     (23, 3)  -> 23 + 3*3 = 32 = 2**5
        D: From C follows: X + n*Y = 2 ** m
            be GCD (x,y) = p , p where p is not divisible by 2 and p > 1, then
                           X + n*Y = p * ( X/p + n*Y/p ) = 2 ** m
                           then 2**m should be divisible by p. But it is not.
            =>  GCD (x,y) must power of 2
        """
        gcd = math.gcd(targetX, targetY)
        return str(f"{gcd:b}").count("1") == 1

    def isReachable_accepted(self, targetX: int, targetY: int) -> bool:
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
    do_test(2, 8, 7, True)
    do_test(3, 16, 7, True)
    do_test(4, 32, 7, True)
    do_test(5, 4, 14, True)
    do_test(6, 4, 28, True)
    do_test(7, 4, 56, True)
    do_test(8, 4, 56, True)
    do_test(9, 8, 14, True)
    do_test(10, 4, 11, True)
    do_test(11, 15, 11, True)
    do_test(12, 15, 22, True)
    do_test(13, 30, 22, True)
    do_test(14, 30, 52, True)
    do_test(15, 30, 82, True)

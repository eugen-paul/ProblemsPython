from math import sqrt

class Solution:
    def mySqrt(self, x: int) -> int:
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
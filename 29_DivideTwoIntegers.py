from math import ceil, floor


min_value = -2**31
max_value = 2**31-1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        resp = (dividend / divisor)
        if resp < 0:
            resp = ceil(resp)
        else:
            resp = floor(resp)
        
        if resp < min_value:
            return min_value
        if resp > max_value:
            return max_value
        return resp
    
    def divide_1(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend > 0 and divisor < 0) \
                or (dividend < 0 and divisor > 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        resp = (dividend // divisor) * sign

        if resp < min_value:
            return min_value
        if resp > max_value:
            return max_value
        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.divide(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 10, 3, 3)
    do_test(1, 7, -3, -2)
    do_test(2, -6, 4, -1)

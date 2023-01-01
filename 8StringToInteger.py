class Solution:
    def myAtoi(self, s: str) -> int:
        response = ""
        dig = False

        for c in s.strip():
            if (c != '-' and c != '+' and not c.isdecimal()) or ((c == '-' or c == '+') and dig):
                break

            if c.isdecimal():
                dig = True

            response += c

        try:
            response = int(response)
        except ValueError:
            response = 0

        if response < -2**31:
            return -2**31
        elif 2**31 - 1 < response:
            return 2**31 - 1
        else:
            return response

    def myAtoi_alt(self, s: str) -> int:
        response = 0
        sign = 1
        sign_read = False
        dig = False

        for c in s.strip():
            if c.isdecimal():
                response = response * 10 + int(c)
                dig = True
            elif c == "-" and not dig and not sign_read:
                sign = -1
                sign_read = True
            elif c == '+' and not dig and not sign_read:
                sign_read = True
            else:
                break

        response *= sign

        if response < -2**31:
            return -2**31
        elif 2**31 - 1 < response:
            return 2**31 - 1
        else:
            return response


def do_test(i: int, s: str, r: int):
    c = Solution()
    resp = c.myAtoi(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


def do_test2(i: int, s: str, r: int):
    c = Solution()
    resp = c.myAtoi_alt(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "42", 42)
    do_test(1, "   -42", -42)
    do_test(2, "4193 with words", 4193)
    do_test(3, "+4193 with words", 4193)
    do_test(4, "+4193-", 4193)

    do_test2(10, "42", 42)
    do_test2(11, "   -42", -42)
    do_test2(12, "4193 with words", 4193)
    do_test2(13, "+4193 with words", 4193)
    do_test2(14, "+4193-", 4193)



def do_test(i: int, s: str, r: int):
    c = Solution()
    resp = c.myAtoi(s)
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

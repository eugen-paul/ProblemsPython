class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        resp = [0] * (len(num1) + len(num2))
        data1 = [int(x) for x in num1]
        data2 = [int(x) for x in num2]

        for i, x in enumerate(reversed(data1)):
            carry = 0
            for j, y in enumerate(reversed(data2)):
                resp[j+i] = x * y + carry + resp[j+i]
                carry = resp[j+i] // 10
                resp[j+i] = resp[j+i] % 10
            if carry != 0:
                resp[j+i+1] = carry + resp[j+i+1]

        while resp[-1] == 0:
            resp.pop()

        return "".join([str(x) for x in reversed(resp)])

    def multiply_simple(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.multiply(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, "2", "3", "6")
    do_test(1, "123", "456", "56088")

class Solution:
    
    def addBinary_4(self, a: str, b: str) -> str:
        cary = 0
        k = 0
        if len(b) > len(a):
            a, b = b, a
        resp = list()
        for a_i in reversed(a):
            if len(b) <= k:
                b_i = 0
            else:
                b_i = b[len(b) - k - 1]
            k += 1
            if cary == 1 and a_i == b_i == "1":
                resp.append("1")
            elif cary == 1 and (a_i == "1" or b_i == "1"):
                resp.append("0")
            elif cary == 1:
                cary = 0
                resp.append("1")
            elif cary == 0 and a_i == b_i == "1":
                cary = 1
                resp.append("0")
            elif cary == 0 and (a_i == "1" or b_i == "1"):
                resp.append("1")
            elif cary == 0:
                resp.append("0")

        if cary == 1:
            resp.append("1")
        return "".join(reversed(resp))

    def addBinary_3(self, a: str, b: str) -> str:
        resp = list()
        a = list(reversed(a))
        b = list(reversed(b))
        if len(b) > len(a):
            a, b = b, a
        while len(b) < len(a):
            b.append("0")

        carry = "0"
        for n, m in zip(a, b):
            if n == "0" and m == "0" and carry == "0":
                resp.append("0")
            elif (n == "0" and m == "0" and carry == "1") \
                    or (n == "1" and m == "0" and carry == "0") \
                    or (n == "0" and m == "1" and carry == "0"):
                resp.append("1")
                carry = "0"
            elif (n == "1" and m == "1" and carry == "0") \
                    or (n == "0" and m == "1" and carry == "1") \
                    or (n == "1" and m == "0" and carry == "1"):
                resp.append("0")
                carry = "1"
            else:
                resp.append("1")
                carry = "1"
        if carry == "1":
            resp.append("1")
        return "".join(reversed(resp))

    def addBinary_2(self, a: str, b: str) -> str:
        a = int(a, base=2)
        b = int(b, base=2)
        return f"{a+b:b}"


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.addBinary(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "11", "1", "100")
    do_test(1, "1010", "1011", "10101")

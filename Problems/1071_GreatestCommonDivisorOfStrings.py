import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        res = ""

        gcd = math.gcd(len(str2), len(str1))

        def check(len_div: int) -> bool:
            divisor1 = str1[:len_div]
            divisor2 = str2[:len_div]

            if divisor1 == divisor2 \
                and divisor1 * (len(str1) // len_div) == str1 \
                    and divisor2 * (len(str2) // len_div) == str2:
                return True

        for i in range(1, math.ceil(gcd ** 0.5)+1):
            if len(str2) % i != 0 or len(str1) % i != 0:
                continue

            if check(i):
                res = str1[:i]

            if gcd % i == 0:
                g = gcd // i
                if check(g):
                    return str1[:g]

        return res

    def gcdOfStrings_1(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        res = ""

        gcd = math.gcd(len(str2), len(str1))

        for i in range(gcd+1, 0, -1):
            if len(str2) % i != 0 or len(str1) % i != 0:
                continue

            divisor1 = str1[:i]
            divisor2 = str2[:i]

            if divisor1 == divisor2 \
                and divisor1 * (len(str1) // i) == str1 \
                    and divisor2 * (len(str2) // i) == str2:
                res = divisor1
                break

        return res


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.gcdOfStrings(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "ABCABC", "ABC", "ABC")
    do_test(1, "ABABAB", "ABAB", "AB")
    do_test(2, "LEET", "CODE", "")
    do_test(3, "ABABABAB", "ABAB", "ABAB")
    do_test(4, "AAAAAAAA", "AAAAAAAA", "AAAAAAAA")
    do_test(5, "A", "AA", "A")

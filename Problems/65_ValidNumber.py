from typing import List


class Solution:

    def isNumber(self, s: str) -> bool:

        pos_e = -1
        for i, c in enumerate(s):
            if c == "e" or c == "E":
                pos_e = i
                break

        def rem_sign(sub: str) -> str:
            if len(sub) == 0:
                return ""
            if sub[0] == "+" or sub[0] == "-":
                sub = sub[1:]
            return sub

        def is_integer(sub: str) -> bool:
            sub = rem_sign(sub)
            if len(sub) == 0:
                return False

            for n in sub:
                if n < "0" or n > "9":
                    return False
            return True

        def is_decimal(sub: str) -> bool:
            sub = rem_sign(sub)
            if len(sub) == 0:
                return False

            dot_count = 0
            dig_count = 0
            for n in sub:
                if n == "." and dot_count == 0:
                    dot_count = 1
                elif n == ".":
                    return False
                elif n >= "0" and n <= "9":
                    dig_count = 1
                else:
                    return False

            return dig_count == 1

        resp = False

        if pos_e == -1:
            # the number mus be a decimal number or an integer
            resp = is_decimal(s) or is_integer(s)
        else:
            # the first number mus be a decimal number or an integer
            # the second number mus be a integer
            first = s[:pos_e]
            second = s[pos_e+1:]
            resp = (is_decimal(first) or is_integer(first)) and is_integer(second)

        return resp

    def isNumber_2(self, s: str) -> bool:
        if s == "inf" \
            or s == "-inf" \
                or s == "+inf" \
                    or s == "Infinity" \
                        or s == "+Infinity" \
                            or s == "-Infinity":
            return False

        try:
            float(s)
        except ValueError:
            return False

        return True

    def isNumber_1(self, s: str) -> bool:
        state = 0

        for c in s:
            if state == 0:
                if c == "+" or c == "-":
                    state = 1
                elif c >= "0" and c <= "9":
                    state = 2
                elif c == ".":
                    state = 31
                else:
                    return False
            elif state == 1:  # read "+" or "-". Need digit or .
                if c >= "0" and c <= "9":
                    state = 2
                elif c == ".":
                    state = 31
                else:
                    return False
            elif state == 2:  # read "+1" or "2". Need digit or e|E or .
                if c >= "0" and c <= "9":
                    state = 2
                elif c == ".":
                    state = 3
                elif c == "e" or c == "E":
                    state = 5
                else:
                    return False
            elif state == 31:  # read "." or "212.". Need digit
                if c >= "0" and c <= "9":
                    state = 4
                else:
                    return False
            elif state == 3:  # read "+141." or "212.". Need digit or e|E
                if c >= "0" and c <= "9":
                    state = 4
                elif c == "e" or c == "E":
                    state = 5
                else:
                    return False
            elif state == 4:  # read "+141.1" or "212.4". Need digit or e|E
                if c >= "0" and c <= "9":
                    state = 4
                elif c == "e" or c == "E":
                    state = 5
                else:
                    return False
            elif state == 5:  # read "+141.1e" or "212.4E". Need digit or +-
                if c >= "0" and c <= "9":
                    state = 7
                elif c == "+" or c == "-":
                    state = 6
                else:
                    return False
            elif state == 6:  # read "+141.1e+" or "212.4E-". Need digit
                if c >= "0" and c <= "9":
                    state = 7
                else:
                    return False
            elif state == 7:  # read "+141.1e+2" or "212.4E-2". Need digit
                if c >= "0" and c <= "9":
                    state = 7
                else:
                    return False

        if state == 6 or state == 1 or state == 5 or state == 31:
            return False
        return True


def do_test(i: int, s, r):
    c = Solution()
    resp = c.isNumber(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "..2", False)
    do_test(0, "0", True)
    do_test(1, "e", False)
    do_test(2, ".", False)
    do_test(3, "0089", True)
    do_test(4, "-0.1", True)
    do_test(5, "+3.14", True)
    do_test(6, "4.", True)
    do_test(7, "-.9", True)
    do_test(8, "2e10", True)
    do_test(9, "-90E3", True)
    do_test(10, "3e+7", True)
    do_test(11, "+6e-1", True)
    do_test(12, "53.5e93", True)
    do_test(13, "-123.456e789", True)
    do_test(14, "abc", False)
    do_test(15, "1a", False)
    do_test(16, "e3", False)
    do_test(17, "99e2.5", False)
    do_test(18, "--6", False)
    do_test(19, "-+3", False)
    do_test(20, "95a54e53", False)
    do_test(21, "+", False)
    do_test(22, "-", False)
    do_test(23, "-e", False)
    do_test(24, "-2e", False)
    do_test(25, ".e1", False)
    do_test(26, ".", False)
    do_test(27, "+.", False)
    do_test(28, "-.", False)

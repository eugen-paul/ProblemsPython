class Solution:

    def myAtoi(self, num: int) -> str:
        roman_values = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        response = ""

        pos = 0
        while num > 0:
            mod = num % 10
            num = num // 10

            if mod == 9:
                response = roman_values[pos] + roman_values[pos+2] + response
            elif 5 <= mod <= 8:
                for _ in range(mod-5):
                    response = roman_values[pos] + response
                response = roman_values[pos+1] + response
            elif mod == 4:
                response = roman_values[pos] + roman_values[pos+1] + response
            elif mod >= 1:
                for _ in range(mod):
                    response = roman_values[pos] + response
            pos += 2

        return response

    def myAtoi_alt(self, num: int) -> str:
        roman_values = (
            (1000, 'M'), (900, 'CM'),
            (500,  'D'), (400, 'CD'),
            (100,  'C'), (90,  'XC'),
            (50,   'L'), (40,  'XL'),
            (10,   'X'), (9,   'IX'),
            (5,    'V'), (4,   'IV'),
            (1,    'I'),
        )
        response = ""
        pos = 0

        while num > 0:
            if num >= roman_values[pos][0]:
                response += roman_values[pos][1]
                num -= roman_values[pos][0]
            else:
                pos += 1

        return response

    def myAtoi_to_slow(self, num: int) -> str:
        roman_values = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        response = []

        pos = 0
        while num > 0:
            mod = num % 10
            num = num // 10

            if mod == 9:
                response.append(roman_values[pos+2])
                response.append(roman_values[pos])
            elif 5 <= mod <= 8:
                for _ in range(mod-5):
                    response.append(roman_values[pos])
                response.append(roman_values[pos+1])
            elif mod == 4:
                response.append(roman_values[pos+1])
                response.append(roman_values[pos])
            elif mod >= 1:
                for _ in range(mod):
                    response.append(roman_values[pos])
            pos += 2

        return "".join(reversed(response))

    def myAtoi_1(self, num: int) -> str:
        response = ""

        t = num // 1000
        for _ in range(t):
            response += "M"

        num = num % 1000

        h = num // 100
        if h == 9:
            response += "CM"
        elif 5 <= h <= 8:
            response += "D"
            for _ in range(h-5):
                response += "C"
        elif h == 4:
            response += "CD"
        elif h >= 1:
            for _ in range(h):
                response += "C"

        num = num % 100

        h = num // 10
        if h == 9:
            response += "XC"
        elif 5 <= h <= 8:
            response += "L"
            for _ in range(h-5):
                response += "X"
        elif h == 4:
            response += "XL"
        elif h >= 1:
            for _ in range(h):
                response += "X"

        num = num % 10

        h = num
        if h == 9:
            response += "IX"
        elif 5 <= h <= 8:
            response += "V"
            for _ in range(h-5):
                response += "I"
        elif h == 4:
            response += "IV"
        elif h >= 1:
            for _ in range(h):
                response += "I"

        return response


def do_test(i: int, s, r):
    c = Solution()
    resp = c.myAtoi_alt(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, "III")
    do_test(1, 58, "LVIII")
    do_test(2, 1994, "MCMXCIV")
    do_test(3, 10, "X")
    do_test(4, 20, "XX")
    do_test(5, 412, "CDXII")
    do_test(6, 999, "CMXCIX")

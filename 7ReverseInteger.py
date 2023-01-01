class Solution:
    def reverse(self, x: int) -> int:
        pos = -1 if x < 0 else 1
        x = x * pos

        s = str(x)[::-1]

        response = int(s) * pos

        if -2**31 <= response <= 2**31 - 1:
            return response
        else:
            return 0

    def reverse_mod(self, x: int) -> int:
        pos = -1 if x < 0 else 1
        x = x * pos

        response = 0

        while x > 0:
            mod = x % 10
            response = response * 10 + mod
            x = x // 10

        response = response * pos

        if -2**31 <= response <= 2**31 - 1:
            return response
        else:
            return 0


if __name__ == "__main__":
    s = Solution()

    t1 = s.reverse(123)
    if t1 == 321:
        print("OK 1")

    t1 = s.reverse(1)
    if t1 == 1:
        print("OK 2")

    t1 = s.reverse(-123)
    if t1 == -321:
        print("OK 3")

    t1 = s.reverse(120)
    if t1 == 21:
        print("OK 4")

    t1 = s.reverse(0)
    if t1 == 0:
        print("OK 5")

    t1 = s.reverse(1534236469)
    if t1 == 0:
        print("OK 6")

    t1 = s.reverse_mod(123)
    if t1 == 321:
        print("OK 1")

    t1 = s.reverse_mod(1)
    if t1 == 1:
        print("OK 2")

    t1 = s.reverse_mod(-123)
    if t1 == -321:
        print("OK 3")

    t1 = s.reverse_mod(120)
    if t1 == 21:
        print("OK 4")

    t1 = s.reverse_mod(0)
    if t1 == 0:
        print("OK 5")

    t1 = s.reverse_mod(1534236469)
    if t1 == 0:
        print("OK 6")

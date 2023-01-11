class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        last_number = self.countAndSay(n-1)

        count = 0
        number = None
        response = ""
        for c in last_number:
            if number is None:
                count = 1
                number = c
                continue
            if number == c:
                count += 1
            else:
                response += str(count) + number
                count = 1
                number = c

        if count != 0:
            response += str(count) + number

        return response


def do_test(i: int, s, r):
    c = Solution()
    resp = c.countAndSay(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 1, "1")
    do_test(1, 4, "1211")

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        state = 0
        resp = 0
        for c in reversed(s):
            if state == 0 and c == " ":
                continue
            else:
                state = 1
                if c == " ":
                    break
                resp += 1

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.lengthOfLastWord(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "Hello World", 5)
    do_test(1, "   fly me   to   the moon  ", 4)
    do_test(2, "luffy is still joyboy", 6)

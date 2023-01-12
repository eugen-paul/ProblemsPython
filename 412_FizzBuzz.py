from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resp = [str(x) for x in range(1, n+1)]

        for i in range(n//3):
            resp[i*3 + 2] = "Fizz"

        for i in range(n//5):
            t = i*5 + 4
            resp[t] = "FizzBuzz" if (t+1) % 3 == 0 else "Buzz"

        return resp

    def fizzBuzz_simple(self, n: int) -> List[str]:
        resp = []
        for i in range(1, n+1):
            mod3 = i % 3
            mod5 = i % 5
            if mod3 == 0 and mod5 == 0:
                resp.append("FizzBuzz")
            elif mod3 == 0:
                resp.append("Fizz")
            elif mod5 == 0:
                resp.append("Buzz")
            else:
                resp.append(str(i))
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.fizzBuzz(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, ["1", "2", "Fizz"])
    do_test(1, 5, ["1", "2", "Fizz", "4", "Buzz"])
    do_test(2, 15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
            "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])

from typing import List


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            return (high - low + 1) // 2
        return (high - low) // 2 + 1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.countOdds(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 7, 3)
    do_test(1, 8, 10, 1)
    do_test(2, 0, 0, 0)
    do_test(3, 0, 1, 1)
    do_test(4, 0, 2, 1)
    do_test(5, 7, 8, 1)
    do_test(6, 6, 7, 1)

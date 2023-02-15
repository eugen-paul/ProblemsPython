from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a = int("".join(str(x) for x in num))
        return [int(x) for x in str(a+k)]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.addToArrayForm(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 0, 0], 34, [1, 2, 3, 4])
    do_test(1, [2, 7, 4], 181, [4, 5, 5])
    do_test(2, [2, 1, 5], 806, [1, 0, 2, 1])

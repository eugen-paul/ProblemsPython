from typing import List, Dict, Tuple, Counter


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = {*nums}
        t = 1
        while t in s:
            t *= 2

        return t


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minImpossibleOR(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 1], 4)
    do_test(1, [5, 3, 2], 1)
    do_test(2, [1, 2, 4, 8], 16)

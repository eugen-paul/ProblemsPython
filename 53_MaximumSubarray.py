from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = 0
        best_max = -1000000

        for n in nums:
            current_max += n
            best_max = max(current_max, best_max)
            if current_max < 0:
                current_max = 0

        return best_max


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxSubArray(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    do_test(1, [1], 1)
    do_test(2, [5, 4, -1, 7, 8], 23)
    do_test(3, [-5, -4, -2, -3, -8], -2)
    do_test(4, [-2, 1], 1)

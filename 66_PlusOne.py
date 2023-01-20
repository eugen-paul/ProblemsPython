from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i, n in enumerate(reversed(digits)):
            s = n + carry
            carry = s // 10
            digits[len(digits) - i - 1] = s % 10
        if carry != 0:
            return [carry] + digits
        return digits

    def plusOne_fast(self, digits: List[int]) -> List[int]:
        i = int("".join([str(x) for x in digits])) + 1
        return [int(x) for x in str(i)]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.plusOne(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3], [1, 2, 4])
    do_test(1, [4, 3, 2, 1], [4, 3, 2, 2])
    do_test(2, [9], [1, 0])

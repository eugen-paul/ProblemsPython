from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        last = nums[0]
        dubl = False
        pos = 1
        for i in range(1, len(nums)):
            if nums[i] != last:
                nums[pos] = nums[i]
                last = nums[i]
                pos += 1
                dubl = False
            elif not dubl:
                dubl = True
                nums[pos] = nums[i]
                pos += 1

        return pos


def do_test(i: int, s, r, n):
    c = Solution()
    resp = c.removeDuplicates(s)
    if resp == r and s[:resp] == n:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)
        print("NOK", i, "expected", n, "response", s[:resp])


if __name__ == "__main__":
    do_test(0, [1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3])
    do_test(1, [0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3])

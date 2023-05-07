from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = [0,0]
        for n in nums:
            if n == 0:
                c[0] += 1
            elif n == 1:
                c[1] += 1
        
        for i in range(c[0]):
            nums[i] = 0
        for i in range(c[0], c[0]+c[1]):
            nums[i] = 1
        for i in range(c[0]+c[1], len(nums)):
            nums[i] = 2


def do_test(i: int, s, r):
    c = Solution()
    c.sortColors(s)
    resp = s
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
    do_test(1, [2, 0, 1], [0, 1, 2])

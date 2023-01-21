from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]

        for i in range(len(nums)-1):
            max_jump = max(max_jump, nums[i] + i)
            
            if max_jump <= i:
                return False

        return True
    
    def canJump_2(self, nums: List[int]) -> bool:
        max_jump = nums[0]

        for i, n in enumerate(nums):
            if i == len(nums)-1:
                return True

            max_jump = max(max_jump, n + i)
            
            if max_jump <= i:
                return False

        return True


def do_test(i: int, s, r):
    c = Solution()
    resp = c.canJump(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, 1, 1, 4], True)
    do_test(1, [3, 2, 1, 0, 4], False)
    do_test(2, [0, 4, 4, 4, 4], False)
    do_test(3, [1, 1, 0, 1, 1], False)
    do_test(4, [1, 1, 0, 1, 1], False)
    do_test(5, [1, 1, 1, 1, 1], True)
    do_test(6, [3, 0, 0, 1, 1], True)
    do_test(7, [3, 0, 0, 1, 0], True)

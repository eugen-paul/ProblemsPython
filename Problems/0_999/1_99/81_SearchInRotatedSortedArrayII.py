from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == target

        l = 0
        r = len(nums) - 1
        m = (l+r)//2

        if nums[m] == target:
            return True

        if nums[l] <= target <= nums[m]:
            return self.search(nums[l:m], target)

        if nums[m] <= target <= nums[r]:
            return self.search(nums[m+1:r+1], target)

        if nums[l] < nums[m]:
            return self.search(nums[m+1:r+1], target)

        if nums[m] < nums[r]:
            return self.search(nums[l:m], target)

        return self.search(nums[l:m], target) or self.search(nums[m+1:r+1], target)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.search(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 5, 6, 0, 0, 1, 2], 0, True)
    do_test(1, [2, 5, 6, 0, 0, 1, 2], 3, False)

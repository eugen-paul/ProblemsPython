from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (r+l) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+1
            else:
                r = m-1

        return l

    def searchInsert_1(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while True:
            if left == right:
                if nums[left] == target:
                    return left
                if nums[left] < target:
                    return left+1
                return left

            m = (left + right) // 2
            m_v = nums[m]
            if target <= m_v:
                right = m
            else:
                left = m+1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.searchInsert(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 5, 6], 5, 2)
    do_test(1, [1, 3, 5, 6], 2, 1)
    do_test(2, [1, 3, 5, 6], 7, 4)

from typing import List, Dict, Tuple, Counter


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l < r:
            m = (r + l) // 2
            if nums[m - 1] != nums[m] != nums[m + 1]:
                return nums[m]

            if (m & 1 == 0 and nums[m] == nums[m + 1]) or (m & 1 == 1 and nums[m - 1] == nums[m]):
                l = m + 1
            else:
                r = m - 1

        return nums[l]

    def singleNonDuplicate_(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums)-1

        while l < r:
            m = (r + l) // 2
            if m > 0 and m < len(nums) - 1 and nums[m - 1] != nums[m] and nums[m] != nums[m + 1]:
                return nums[m]

            if (m % 2 == 0 and nums[m] == nums[m + 1]) or (m % 2 == 1 and nums[m - 1] == nums[m]):
                l = m + 1
            else:
                r = m - 1

        return nums[l]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.singleNonDuplicate(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 1, 2, 3, 3, 4, 4, 8, 8], 2)
    do_test(1, [3, 3, 7, 7, 10, 11, 11], 10)
    do_test(2, [3], 3)
    do_test(3, [1, 1, 3, 3, 4, 4, 8, 8, 9], 9)
    do_test(4, [1, 4, 4, 8, 8, 9, 9], 1)
    do_test(5, [1, 1, 2, 3, 3], 2)
    do_test(6, [1, 3, 3], 1)
    do_test(7, [1, 1, 3], 3)

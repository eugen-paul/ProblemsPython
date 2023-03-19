from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sl = list(nums)
        sl.sort()

        start = 0
        end = len(sl)-1
        s = sl[start] + sl[end]

        while s != target:
            if s > target:
                end -= 1
            else:
                start += 1
            s = sl[start] + sl[end]

        p1 = nums.index(sl[start])
        if sl[start] == sl[end]:
            p2 = nums.index(sl[end], p1 + 1)
        else:
            p2 = nums.index(sl[end])

        return sorted([p1, p2])


if __name__ == "__main__":
    s = Solution()
    if s.twoSum(list([2, 7, 11, 15]), 9) == [0, 1]:
        print("OK")
    if s.twoSum(list([3, 2, 4]), 6) == [1, 2]:
        print("OK")
    if s.twoSum(list([-1, -2, -3, -4, -5]), -8) == [2, 4]:
        print("OK")

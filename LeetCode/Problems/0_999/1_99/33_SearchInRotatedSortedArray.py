from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums) // 2
        if len(nums) == 0:
            return -1
        if nums[m] == target:
            return m
        if nums[0] <= target and target < nums[m]:
            return self.search(nums[:m], target)
        elif nums[m] < target and target <= nums[-1]:
            tmp = self.search(nums[m+1:], target)
            return tmp + m + 1 if tmp != -1 else -1
        else:
            if nums[0] > nums[m]:
                return self.search(nums[:m], target)
            if nums[m] > nums[-1]:
                tmp = self.search(nums[m+1:], target)
                return tmp + m + 1 if tmp != -1 else -1
        return -1

    def search_1(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while True:
            if left > right:
                return -1

            if left == right:
                if nums[left] == target:
                    return left
                return -1

            l_v = nums[left]
            m_v = nums[(left+right)//2]
            r_v = nums[right]

            if l_v <= target <= m_v:
                right = (left+right)//2
            elif m_v+1 <= target <= r_v:
                left = (left+right)//2+1
            elif l_v <= m_v:
                left = (left+right)//2+1
            else:
                right = (left+right)//2

    def s(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l > r:
            return -1

        if l == r:
            if nums[l] == target:
                return l
            return -1

        l_v = nums[l]
        m_v = nums[(l+r)//2]
        r_v = nums[r]

        if l_v <= target <= m_v:
            return self.s(nums, target, l, (l+r)//2)

        if m_v+1 <= target <= r_v:
            return self.s(nums, target, (l+r)//2+1, r)

        if l_v <= m_v:
            return self.s(nums, target, (l+r)//2+1, r)
        else:
            return self.s(nums, target, l, (l+r)//2)

    def search_rec(self, nums: List[int], target: int) -> int:
        return self.s(nums, target, 0, len(nums)-1)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.search(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [4, 5, 6, 7, 0, 1, 2], 0, 4)
    do_test(1, [4, 5, 6, 7, 0, 1, 2], 3, -1)
    do_test(3, [1], 0, -1)
    do_test(4, [5, 1, 3], 5, 0)
    do_test(5, [1, 3, 5], 5, 2)

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        return self.s(nums, target, 0, len(nums)-1)

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

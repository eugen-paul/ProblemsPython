from typing import List


class Solution:

    def s(self, nums: List[int], target: int, l: int, r: int, search_max: bool) -> int:
        if l > r:
            return -1

        if l == r:
            if nums[l] == target:
                return l
            return -1

        m_v_l = nums[(l+r)//2]
        m_v_r = nums[(l+r)//2+1]

        in_min = target <= m_v_l
        in_max = m_v_r <= target
        
        just_in_min = in_min and not in_max
        in_both = in_min and in_max

        if (just_in_min) \
                or (in_both and not search_max):
            return self.s(nums, target, l, (l+r)//2, search_max)

        return self.s(nums, target, (l+r)//2+1, r, search_max)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mi = self.s(nums, target, 0, len(nums)-1, False)
        if mi == -1:
            return [-1, -1]
        ma = self.s(nums, target, 0, len(nums)-1, True)
        return [mi, ma]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.searchRange(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [5, 7, 7, 8, 8, 10], 8, [3, 4])
    do_test(1, [5, 7, 7, 8, 8, 10], 6, [-1, -1])
    do_test(2, [], 0, [-1, -1])

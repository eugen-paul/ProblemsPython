from typing import Dict, List


class Solution:

    mem_jumps: List[int]

    def do_jump(self, nums: List[int], start: int, current) -> int:
        if start >= len(nums) - 1:
            return 0

        mem = self.mem_jumps[start]
        if mem != -1:
            return mem

        max_len = nums[start]

        best = 1_000_000

        for i in range(1, max_len + 1):
            best = min(best, self.do_jump(nums, start + i, current + 1) + 1)

        self.mem_jumps[start] = best

        return best

    def jump(self, nums: List[int]) -> int:
        self.mem_jumps = [-1] * len(nums)
        return self.do_jump(nums, 0, 0)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.jump(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 3, 1, 1, 4], 2)
    do_test(1, [2, 3, 0, 1, 4], 2)
    do_test(2, [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6,
            5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5], 5)
    do_test(3, [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7, 0, 3, 4, 8,
            3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5], 13)

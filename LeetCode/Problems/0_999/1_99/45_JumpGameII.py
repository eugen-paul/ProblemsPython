from typing import Dict, List


class Solution:

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 0
        last_max_jump = nums[0]
        max_jump = nums[0]

        for i,n in enumerate(nums):
            if i > last_max_jump:
                jumps+=1
                last_max_jump = max_jump
            max_jump = max(max_jump, n+i)

        return jumps+1
    
    def jump_2(self, nums: List[int]) -> int:
        jumps = 0
        i = 0

        while i < len(nums)-1:
            max_target = 0
            max_index = 0
            for j in range(1, nums[i]+1):
                # check if the endpoint has been reached.
                if i+j >= len(nums) - 1:
                    max_index = i+j
                    break
                # search for the point that will take me the farthest on the next jump.
                if max_target < nums[i+j] + i + j:
                    max_target = nums[i+j] + i + j
                    max_index = i+j
            jumps += 1
            # Make the jump to previously found point
            i = max_index

        return jumps

    mem_jumps: List[int]
    best_resp: int

    def do_jump(self, nums: List[int], start: int, current) -> int:
        if start >= len(nums) - 1:
            self.best_resp = min(current, self.best_resp)
            return 0

        if current >= self.best_resp:
            return 1_000_000

        mem = self.mem_jumps[start]
        if mem != -1:
            return mem

        max_len = nums[start]

        best = 1_000_000

        for i in range(1, max_len + 1):
            best = min(best, self.do_jump(nums, start + i, current + 1) + 1)

        self.mem_jumps[start] = best

        return best

    def jump_recursive(self, nums: List[int]) -> int:
        self.mem_jumps = [-1] * len(nums)
        self.best_resp = 1_000_000
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

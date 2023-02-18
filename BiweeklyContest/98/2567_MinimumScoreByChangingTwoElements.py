from typing import List, Dict, Tuple, Counter


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-3] - nums[0], nums[-2] - nums[1], nums[-1] - nums[2])


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minimizeSum(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 4, 3], 0)
    do_test(1, [1, 4, 7, 8, 5], 3)
    do_test(2, [1, 2, 3, 1000], 1)

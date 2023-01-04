from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        m = {}
        for current in nums:
            counter = m.get(current, 0)
            m[current] = counter+1

        k = [key for key in m]
        k.sort()

        best_target = 50_000

        for i, current in enumerate(k):
            left = i if m[current] >= 2 else i+1
            right = len(k)-1

            while left <= right:
                if left == right and (m[k[left]] == 1 or (m[k[left]] == 2 and left == i)):
                    break
                s = current + k[left] + k[right]
                if abs(target - best_target) > abs(target - s):
                    best_target = s

                if s == target:
                    return target
                elif s > target:
                    right -= 1
                else:
                    left += 1

        return best_target

    def threeSumClosest_slow(self, nums: List[int], target: int) -> int:
        nums.sort()

        best_target = 50_000

        for i, current in enumerate(nums):
            left = i+1
            right = len(nums)-1

            while left < right:
                s = current + nums[left] + nums[right]
                if s == target:
                    return target
                elif s > target:
                    right -= 1
                else:
                    left += 1

                if abs(target - best_target) > abs(target - s):
                    best_target = s

        return best_target


def do_test(i: int, s, s1, r):
    c = Solution()
    resp = c.threeSumClosest(s, s1)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [-1, 2, 1, -4], 1, 2)
    do_test(1, [0, 0, 0], 1, 0)
    do_test(2, [0, 0, 0], 10, 0)
    do_test(3, [0, 0, 0, 1], 10, 1)
    do_test(4, [1, 2, 3, 4], 6, 6)
    do_test(5, [-100, -98, -2, -1], -101, -101)
    do_test(6, [-100, -98, -2, -1, 1000, 1001, 1002, 1003, 1004], -101, -101)
    do_test(7, [-100, 1, 1, 2, 3, 4], 1, 4)

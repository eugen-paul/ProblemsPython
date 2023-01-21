from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        left = 0
        right = len(height) - 1
        current_height = min(height[left], height[right])
        area = (right - 1) * current_height

        while left < right-1:
            if height[left] > height[right]:
                right -= 1
                area -= min(current_height, height[right])
            else:
                left += 1
                area -= min(current_height, height[left])

            if current_height < height[right] and current_height < height[left]:
                new_height = min(height[left], height[right])
                area += (new_height - current_height) * (right - left - 1)
                current_height = new_height

        return area


def do_test(i: int, s, r):
    c = Solution()
    resp = c.trap(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
    do_test(1, [4, 2, 0, 3, 2, 5], 9)
    do_test(2, [4], 0)
    do_test(3, [4, 5], 0)

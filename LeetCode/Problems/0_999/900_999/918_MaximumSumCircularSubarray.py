from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        left = 0
        right = 0

        max_sum = nums[0]
        current_sum = nums[0]

        for _ in range(len(nums) * 2):

            while left != right and (current_sum < 0 or nums[left] < 0):
                current_sum -= nums[left]
                max_sum = max(max_sum, current_sum)
                left = (left + 1) % len(nums)

            right = (right + 1) % len(nums)

            if right == left:
                left = (left + 1) % len(nums)
                best_left = left
                left_best_sum = current_sum
                while left != right and current_sum != max_sum:
                    current_sum -= nums[left]
                    left = (left + 1) % len(nums)
                    if left_best_sum < current_sum:
                        left_best_sum = current_sum
                        best_left = left
                left = best_left
                current_sum = left_best_sum
            else:
                current_sum += nums[right]

            max_sum = max(max_sum, current_sum)

        return max_sum

    def maxSubarraySumCircular_web(self, nums):
        # kadane's algo
        def kadane(nums):
            local_sum = nums[0]
            global_sum = nums[0]
            for i in range(1, len(nums)):
                local_sum = max(nums[i], local_sum + nums[i])
                global_sum = max(global_sum, local_sum)
            return global_sum
        # case 1: max subarray sum in [0 .. n - 1]
        # i.e. kadane's algo
        # case 2. circular subarray in [0 .. |  n - 1 .. | .. 2 * n - 1]
        # i.e. total sum - min subarray sum in [0 .. n - 1]
        n = len(nums)
        # use kadane's algo to find out max sub array sum (case 1)
        max_sub_array_sum = kadane(nums)
        # handle cases like [-3,-2,-3]
        if max_sub_array_sum < 0:
            return max_sub_array_sum
        # calculate the total sum
        total_sum = sum(nums)
        # in order to use the same kadane function, we flip the sign
        for i in range(n):
            nums[i] *= -1
        # use kadane's algo to find out min sub array sum
        min_sub_array_sum = kadane(nums) * -1
        # compare case 1 & case 2, take the max
        return max(max_sub_array_sum, total_sum - min_sub_array_sum)

    def maxSubarraySumCircular_slow(self, nums: List[int]) -> int:
        best = -4 * 10**4
        best_t = (0, 0)

        for start in range(len(nums)):
            s = 0
            for end in range(len(nums)):
                s += nums[(start + end) % len(nums)]
                if best < s:
                    best = s
                    best_t = (start, end)

        print(best_t)
        return best


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxSubarraySumCircular(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, -2, 3, -2], 3)
    do_test(1, [5, -3, 5], 10)
    do_test(2, [-3, -2, -3], -2)
    do_test(3, [1, 2, 3, -1, 2, 3, 4], 15)
    do_test(4, [1, 2, 3, -1, -2, 3, 4], 13)
    do_test(5, [-1000, 2, 3, -1000, 2, 3, 4], 9)
    do_test(6, [-1000, 2, 3, -1000, 2, 3, -1000], 5)
    do_test(7,
            [52, 183, 124, 154, -170, -191, -240, 107, -178, 171, 75, 186, -125, 61, -298, 284, 21, -73, -294, 253, 146, 248, -248, 127, 26, 289, 118, -22, -300, 26, -116, -113, -44, 29, 252, -278, 47, 254, -106, 246, -275, 42, 257, 15, 96, -298, -69, -104, -239, -95, -4, 76, -202, 156, -14, -178, 188, -84, 78, -195, -125, 28, 109, 125, -25, -53, 58, 287, 55, -296, 198, 281, 53, -160, 146, 298, 25, -41, -3, 27, -242, 169, 287, -281, 19, 91, 213, 115, 211, -218, 124, -25, -272, 278, 296, -177, -166, -192, 97, -49, -25, 168, -81, 6, -94, 267, 293, 146, -1, -258, 256, 283, -156, 197, 28, 78, 267, -151, -230, -66, 100, -94, -66, -123, 121, -214, -182, 187, 65, -186, 215, 273, 243, -99, -76, 178, 59, 190, 279, 300, 217, 67, -117, 170, 163, 153, -37, -147, -251, 296, -176,
                117, 68, 258, -159, -300, -36, -91, -60, 195, -293, -116, 208, 175, -100, -97, 188, 79, -270, 80, 100, 211, 112, 264, -217, -142, 5, 105, 171, -264, -247, 138, 275, 227, -86, 30, -219, 153, 10, -66, 267, 22, -56, -70, -234, -66, 89, 182, 110, -146, 162, -48, -201, -240, -225, -15, -275, 129, -117, 28, 150, 84, -264, 249, -85, 70, -140, -259, 26, 162, 5, -203, 143, 184, 101, 140, 207, 131, 177, 274, -178, -79, 14, -36, 104, 52, 31, 257, 273, -52, 74, 276, 104, -133, -255, 188, -252, 229, 200, -74, -39, -250, 142, -201, -196, -43, -40, 255, -149, -299, -197, -175, -96, -155, -196, -24, 12, 79, 71, -144, -59, -120, 227, -256, -163, -297, 116, 286, -283, -31, -221, -41, 121, -170, 160, 205, 8, 88, 25, -272, -107, 292, -180, 299, 94, -97, -81, -134, 37, 238],
            5803)

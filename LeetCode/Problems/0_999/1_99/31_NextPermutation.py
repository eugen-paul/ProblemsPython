from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        last = None
        for i, c in enumerate(reversed(nums)):
            if last is None:
                last = c
                continue
            # Search from right to left the first tupel, which is in descending order.
            if last > c:
                # Find in all digits on the right side of the tupel the smallest number that is greater than the left number in the tupel.
                best_target = last
                best_pos = len(nums) - i
                for j in range(len(nums) - i, len(nums)):
                    if best_target > nums[j] and c < nums[j]:
                        best_target = nums[j]
                        best_pos = j
                # Swap the found number with the left number from the tuple.
                nums[best_pos] = c
                nums[len(nums) - i - 1] = best_target
                # Sort all numbers on the right side including the right number from the tuple in ascending order.
                if i >= 2:
                    # Here you could sort the sub-array by hand to save memory.
                    sub_array = nums[len(nums) - i:]
                    sub_array.sort()
                    for j, n in enumerate(sub_array):
                        nums[len(nums) - i+j] = n
                return
            last = c

        # No tuples in descending order were found. It is the last sequence of the permutation.
        # Reverse the array.
        for i in range(len(nums) // 2):
            nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]

    def nextPermutation_off(self, nums: List[int]) -> None:
        last = nums[-1]
        for i, c in enumerate(reversed(nums)):
            # Search from right to left the first tupel, which is in descending order.
            if last > c:
                # Find in all digits on the right side of the tupel the smallest number that is greater than the left number in the tupel.
                best_target = last
                best_pos = len(nums) - i
                for j in range(len(nums) - i, len(nums)):
                    if best_target >= nums[j] and c < nums[j]:
                        best_target = nums[j]
                        best_pos = j
                # Swap the found number with the left number from the tuple.
                nums[best_pos] = c
                nums[len(nums) - i - 1] = best_target
                # Reverse all numbers on the right side excluding the right number.
                if i >= 2:
                    # Here you could sort the sub-array by hand to save memory.
                    sub_array = nums[len(nums) - i:]
                    sub_array.reverse()
                    for j, n in enumerate(sub_array):
                        nums[len(nums) - i + j] = n
                return
            last = c

        # No tuples in descending order were found. It is the last sequence of the permutation.
        # Reverse the array.
        for i in range(len(nums) // 2):
            nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]


def do_test(i: int, s, r):
    c = Solution()
    c.nextPermutation_off(s)
    if s == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", s)


if __name__ == "__main__":
    do_test(0, [1, 2, 3], [1, 3, 2])
    do_test(1, [3, 2, 1], [1, 2, 3])
    do_test(2, [1, 1, 5], [1, 5, 1])
    do_test(3, [1], [1])
    do_test(4, [1, 1, 1], [1, 1, 1])
    do_test(5, [1, 3, 2], [2, 1, 3])
    do_test(6, [2, 1, 3], [2, 3, 1])
    do_test(7, [2, 3, 1], [3, 1, 2])
    do_test(8, [3, 1, 2], [3, 2, 1])
    do_test(9, [1, 1, 2, 1, 1, 1], [1, 2, 1, 1, 1, 1])
    do_test(10, [1, 1, 2, 1, 2, 1], [1, 1, 2, 2, 1, 1])
    do_test(11, [1, 1, 2, 2, 1, 1], [1, 2, 1, 1, 1, 2])
    do_test(12, [1, 3, 2, 0], [2, 0, 1, 3])

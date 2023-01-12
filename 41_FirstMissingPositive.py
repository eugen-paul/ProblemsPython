from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Advanced version of the dumb solution. Instead of storing the data in an extra array, 
        the data is stored in input array. For this the actual data is shifted 1 bit to the left. 
        The last bit at element N is set, if a value N+1 was read in the array.
        """
        for i, n, in enumerate(nums):
            if n < 1 or n > len(nums):
                # set all illegal values to 0
                nums[i] = 0
            else:
                # shift all legal values
                nums[i] = nums[i] << 2

        #set last bit of nums[n] in n is in nums
        for i, n in enumerate(nums):
            v = n >> 2
            if v > 0:
                nums[v-1] = nums[v-1] | 1

        #response first i with nums[i] is even (last bit is not set)
        for i in range(len(nums)):
            if nums[i] & 1 == 0:
                return i+1
        return len(nums)+1

    def firstMissingPositive_web(self, nums: List[int]) -> int:
        def swap(nums: List[int], i: int, j: int):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        length = len(nums)
        for index in range(len(nums)):
            while (nums[index] > 0 and nums[index] <= length and nums[nums[index] - 1] != nums[index]):
                swap(nums, index, nums[index] - 1)

        for index in range(len(nums)):
            if nums[index] != index + 1:
                return index + 1
        return length + 1

    def firstMissingPositive_dumb(self, nums: List[int]) -> int:
        d = [x for x in range(len(nums)+2)]

        for n in nums:
            if n >= 1 and n <= len(nums):
                d[n] = None

        d[0] = None
        for n in d:
            if n is not None:
                return n
        return len(d)

    def firstMissingPositive_simple(self, nums: List[int]) -> int:
        s = sorted(nums)
        next_n = 1
        for x in s:
            if next_n > x:
                continue
            if next_n != x:
                return next_n
            next_n += 1
        return next_n


def do_test(i: int, s, r):
    c = Solution()
    resp = c.firstMissingPositive(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 0], 3)
    do_test(1, [3, 4, -1, 1], 2)
    do_test(2, [7, 8, 9, 11, 12], 1)
    do_test(3, [2, -1, -2, 8, 9, 11, 12], 1)
    do_test(4, [3, 4, 5, 6, 2, 1, 7], 8)
    do_test(5, [3, 4, 6, 2, 1, 7], 5)
    do_test(6, [1], 2)
    do_test(7, [2], 1)
    do_test(8, [0], 1)
    do_test(9, [-1], 1)

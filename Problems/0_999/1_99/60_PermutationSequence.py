from itertools import permutations
import math
from typing import List


class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        remaining_digits = [x for x in range(1, n+1)]
        resp = list()

        # we calculate from 0 to n => increment k, since k is from 1 to n+1.
        k -= 1

        while len(remaining_digits) > 0:
            # calculate the number of permutations of all possible remaining digits.
            f = math.factorial(len(remaining_digits))
            # The first digit in the permutations is always ascending. Calculate the block length of the digit.
            nm = f // len(remaining_digits)
            # Find out in which block the permutation you are looking for is located.
            p = k // nm
            # Extend the result by the digit and delete the digit from the rest digit list.
            resp.append(remaining_digits[p])
            remaining_digits.pop(p)
            # fit k for further search
            k = k % nm

        return "".join(str(x) for x in resp)

    def getPermutation_slow(self, n: int, k: int) -> str:
        perm = permutations([x for x in range(1, n+1)])

        return "".join(str(x) for x in list(perm)[k-1])

    def nextPermutation(self, nums: List[int]) -> None:
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

    def getPermutation_very_slow(self, n: int, k: int) -> str:
        """using 31_NextPermutation."""
        perm = [x for x in range(1, n+1)]

        for _ in range(k-1):
            self.nextPermutation(perm)

        return "".join(str(x) for x in perm)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.getPermutation(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, 3, "213")
    do_test(1, 4, 9, "2314")
    do_test(2, 3, 1, "123")
    do_test(3, 4, 1, "1234")
    do_test(4, 4, 2, "1243")
    do_test(5, 4, 3, "1324")
    do_test(6, 4, 4, "1342")
    do_test(7, 4, 5, "1423")
    do_test(8, 4, 6, "1432")
    do_test(9, 4, 7, "2134")
    do_test(10, 4, 8, "2143")
    do_test(11, 4, 9, "2314")
    do_test(12, 4, 10, "2341")
    do_test(13, 4, 11, "2413")
    do_test(14, 4, 12, "2431")
    do_test(15, 4, 13, "3124")
    do_test(16, 4, 14, "3142")
    do_test(17, 4, 15, "3214")
    do_test(18, 4, 16, "3241")
    do_test(19, 4, 17, "3412")
    do_test(20, 4, 18, "3421")
    do_test(21, 4, 19, "4123")
    do_test(22, 4, 20, "4132")
    do_test(23, 4, 21, "4213")
    do_test(24, 4, 22, "4231")
    do_test(25, 4, 23, "4312")
    do_test(26, 4, 24, "4321")

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        count = 0
        for x in nums:
            if x != val:
                nums[pos] = x
                pos += 1
                count += 1
        return count


def do_test(i: int, s, d, n, r):
    c = Solution()
    resp = c.removeElement(s, d)
    if resp == n and sorted(s[:resp]) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", sorted(r), "response", sorted(s[:resp]))


if __name__ == "__main__":
    do_test(0, [3, 2, 2, 3], 3, 2, [2, 2])
    do_test(1, [0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 4, 0, 3])
    do_test(2, [], 0, 0, [])
    do_test(3, [1, 2, 3, 4, 5, 6], 6, 5, [1, 2, 3, 4, 5])
    do_test(4, [1, 1, 1, 1, 1], 1, 0, [])
    do_test(5, [1, 1, 1, 1, 2, 2, 2, 2, 2, 2], 2, 4, [1, 1, 1, 1])

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = -1000
        pos = 0
        count = 0
        for c in nums:
            if c != last:
                nums[pos] = c
                last = c
                count += 1
                pos += 1

        return count


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.removeDuplicates(s)
    if resp == n and s[:resp] == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", s[:resp+1])


if __name__ == "__main__":
    do_test(0, [1, 1, 2], 2, [1, 2])
    do_test(1, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
    do_test(2, [], 0, [])
    do_test(3, [1, 2, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5, 6])
    do_test(4, [1, 1, 1, 1, 1], 1, [1])
    do_test(5, [1, 1, 1, 1, 2, 2, 2, 2, 2, 2], 2, [1, 2])

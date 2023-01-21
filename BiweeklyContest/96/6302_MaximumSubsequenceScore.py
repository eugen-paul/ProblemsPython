from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """FAIL"""
        pass


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.maxScore(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 3, 3, 2], [2, 1, 3, 4], 3, 12)
    do_test(1, [4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1, 30)
    do_test(2, [7, 5, 10, 9, 6], [4, 2, 3, 1, 1], 1, 30)
    do_test(3, [4, 2], [7, 5], 2, 30)
    do_test(4, [1, 3], [2, 1], 1, 3)

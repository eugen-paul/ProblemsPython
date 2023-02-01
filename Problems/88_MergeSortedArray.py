from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        p1, p2, t = 0, 0, 0
        c = [0] * (m+n)
        while t < len(c):
            if p1 < m and p2 < n and nums1[p1] <= nums2[p2]:
                c[t] = nums1[p1]
                p1 += 1
            elif p1 < m and p2 < n and nums1[p1] > nums2[p2]:
                c[t] = nums2[p2]
                p2 += 1
            elif p1 < m:
                c[t] = nums1[p1]
                p1 += 1
            else:
                c[t] = nums2[p2]
                p2 += 1
            t += 1

        for i, n in enumerate(c):
            nums1[i] = n

    def merge(self, nums1, m, nums2, n):
        """internet Solution"""
        # move from right to left
        end_1 = m - 1
        end_2 = n - 1
        end_target = m + n - 1
        while end_2 >= 0:
            if end_1 >= 0 and nums1[end_1] > nums2[end_2]:
                nums1[end_target] = nums1[end_1]
                end_target -= 1
                end_1 -= 1
            else:
                nums1[end_target] = nums2[end_2]
                end_target -= 1
                end_2 -= 1

    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()


def do_test(i: int, s, k, l, m, r):
    c = Solution()
    resp = c.merge(s, k, l, m)
    if s == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", s)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    do_test(1, [4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6])
    do_test(2, [1], 1, [], 0, [1])
    do_test(3, [0], 0, [1], 1, [1])
    do_test(4, [0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3])
    do_test(5, [1, 4, 6, 0, 0, 0], 3, [2, 5, 7], 3, [1, 2, 4, 5, 6, 7])
    do_test(6, [1, 4, 6, 0, 0, 0], 3, [2, 3, 7], 3, [1, 2, 3, 4, 6, 7])

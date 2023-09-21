from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2
        a.sort()
        if len(a) % 2 == 1:
            return a[len(a) // 2]
        return (a[len(a) // 2 - 1] + a[len(a) // 2]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_length = len(nums1) + len(nums2)
        half = full_length // 2

        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A

        left_1 = 0
        right_1 = len(A) - 1

        while True:
            mid1 = (right_1 - left_1) // 2 + left_1
            mid2 = half - mid1 - 2  # mid2 is gt -1, because A <= B

            a_last = A[mid1] if mid1 >= 0 and mid1 < len(A) else -(10**7)
            a_next = A[mid1+1] if mid1 >= -1 and mid1 < len(A)-1 else 10**7

            b_last = B[mid2] if mid2 >= 0 and mid2 < len(B) else -(10**7)
            b_next = B[mid2+1] if mid2 >= -1 and mid2 < len(B)-1 else 10**7

            if a_last > b_next:
                right_1 = mid1 - 1
            elif b_last > a_next:
                left_1 = mid1 + 1
            elif full_length % 2 == 1:
                return min(a_next, b_next)
            else:
                return (max(a_last, b_last) + min(a_next, b_next)) / 2


if __name__ == "__main__":
    s = Solution()
    if s.findMedianSortedArrays([1, 3], [2]) == 2.0:
        print("Ok 1")
    if s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5:
        print("Ok 2")
    if s.findMedianSortedArrays([1, 3], [2, 7]) == 2.5:
        print("Ok 3")
    if s.findMedianSortedArrays([1], []) == 1.0:
        print("Ok 4")
    if s.findMedianSortedArrays([], [1]) == 1.0:
        print("Ok 5")

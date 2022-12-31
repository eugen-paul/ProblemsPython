from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = list()
        pos2 = 0
        for i in nums1:
            while pos2 < len(nums2) and nums2[pos2] < i:
                merge.append(nums2[pos2])
                pos2 += 1
            merge.append(i)

        while pos2 < len(nums2):
            merge.append(nums2[pos2])
            pos2 += 1

        if len(merge) % 2 == 0:
            return (merge[len(merge) // 2 - 1] + merge[len(merge) // 2]) / 2

        return merge[len(merge) // 2]


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

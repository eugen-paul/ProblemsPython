from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        se2 = set(nums2)
        for i in nums1:
            if i in se2:
                return i
        
        return -1
    
    def getCommon_accepted(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        
        overlaps = set1 & set2
        
        if len(overlaps) == 0:
            return -1
        
        overlaps = list(overlaps)
        overlaps.sort()
        
        return overlaps[0]
        
def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.getCommon(s,n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1,2,3], [2,4], 2)
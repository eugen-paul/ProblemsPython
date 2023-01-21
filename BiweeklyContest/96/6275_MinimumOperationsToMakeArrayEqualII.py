from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:

        if k == 0:
            if nums1 == nums2:
                return 0
            return -1
        
        delta = 0
        count = 0

        for i in range(len(nums1)):
            if nums1[i] == nums2[i]:
                continue
            need = 0
            if nums1[i] > nums2[i]:
                need = nums1[i] - nums2[i]

                if delta < 0:
                    if abs(delta) > need:
                        delta += need
                        need = 0
                    else:
                        need += delta
                        delta = 0

                if need % k != 0:
                    return -1
                count += need // k
                delta += need

            if nums1[i] < nums2[i]:
                need = nums2[i] - nums1[i]

                if delta > 0:
                    if delta > need:
                        delta -= need
                        need = 0
                    else:
                        need -= delta
                        delta = 0

                if need % k != 0:
                    return -1
                count += need // k
                delta -= need

        if delta != 0:
            return -1
        return count


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.minOperations(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [4, 3, 1, 4], [1, 3, 7, 1], 3, 2)
    do_test(1, [3, 8, 5, 2], [2, 4, 1, 6], 1, -1)
    do_test(2, [4], [2], 2, -1)
    do_test(3, [4, 6], [2, 8], 2, 1)
    do_test(4, [4, 6], [4, 6], 0, 0)
    do_test(5, [4, 6], [4, 7], 0, -1)

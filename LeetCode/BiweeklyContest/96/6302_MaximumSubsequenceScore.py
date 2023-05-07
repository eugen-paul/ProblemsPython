from heapq import heappop, heappush
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """Solution from Leaderboard (17 Yawn_Sean)"""
        # put both arrays to array of tupples and sort it by second array in decr order
        tmp = list(zip(nums1, nums2))
        tmp.sort(key=lambda x: -x[1])

        note = []
        ans = 0
        tot = 0
        # for each tupple do:
        for num1, num2 in tmp:
            # add num1-element to sorted-List
            heappush(note, num1)
            # add num1-element to current sum
            tot += num1

            # At the beginning (as long as you have read less than k elements) the num1 are added together.
            if len(note) > k:
                # After reading more than k elements, you have to throw out the smallest element, because we want to have the bigger sum.
                tot -= heappop(note)
            if len(note) == k:
                # Calculate current value and accept it if it is greater than best.
                # From my point of view, a case could occur here where the currently read digit is removed from the sum.
                # After that, the new scope would be calculated with the current num2. As a consequence the scope will be invalid.
                # This case can be ignored. Because the calculated scope will always be smaller or equal to the current scope.
                ans = max(ans, tot * num2)

        return ans

    def maxScore_accepted(self, nums1: List[int], nums2: List[int], k: int) -> int:
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

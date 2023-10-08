from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        @cache
        def solve(p1: int, p2: int) -> int:
            if p1 == n1 or p2 == n2:
                return None

            ans = nums1[p1] * nums2[p2]
            v1 = solve(p1+1, p2+1)
            if v1 is not None:
                ans = max(ans, ans + v1)

            v2 = solve(p1+1, p2)
            if v2 is not None:
                ans = max(ans, v2)

            v3 = solve(p1, p2+1)
            if v3 is not None:
                ans = max(ans, v3)

            return ans
        return solve(0, 0)

    def maxDotProduct_s(self, nums1: List[int], nums2: List[int]) -> int:
        """sample solution"""
        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            use = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(use, dp(i + 1, j), dp(i, j + 1))

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        return dp(0, 0)

    def maxDotProduct_s(self, nums1: List[int], nums2: List[int]) -> int:
        """sample solution"""
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + dp[i + 1][j + 1]
                dp[i][j] = max(use, dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]

def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maxDotProduct(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 1, -2, 5], [3, 0, -6], 18)
    do_test(1, [3, -2], [2, -6, 7], 21)
    do_test(2, [-1, -1], [1, 1], -1)
    do_test(3, [-5, -1, -2], [3, 3, 5, 5], -3)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

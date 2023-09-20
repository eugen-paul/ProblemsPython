import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:
        s, b = [0], [0]
        for n in nums:
            s.append(s[-1]+n)
        for n in reversed(nums):
            b.append(b[-1]+n)

        l, r = 0, len(b)-1
        ans = inf
        while l+r <= len(nums):
            while r > 0 and s[l] + b[r-1] >= x:
                r -= 1
            if s[l] + b[r] == x:
                ans = min(ans, l+r)
            l += 1
            while r > 0 and s[l] + b[r-1] >= x:
                r -= 1
        return ans if ans != inf and ans <= len(nums) else -1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minOperations(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 1, 4, 2, 3], 5, 2)
    do_test(1, [5, 6, 7, 8, 9], 4, -1)
    do_test(2, [3, 2, 20, 1, 1, 3], 10, 5)
    do_test(3, [5, 2, 3, 1, 1], 5, 1)
    do_test(4, [1, 1], 3, -1)
    do_test(5, [5, 1], 5, 1)
    do_test(6, [1, 5], 5, 1)
    do_test(7, [5207, 5594, 477, 6938, 8010, 7606, 2356, 6349, 3970, 751, 5997, 6114, 9903, 3859, 6900, 7722, 2378, 1996, 8902, 228, 4461, 90, 7321, 7893, 4879, 9987, 1146, 8177, 1073, 7254, 5088, 402, 4266, 6443, 3084, 1403, 5357, 2565, 3470, 3639, 9468, 8932, 3119, 5839, 8008, 2712, 2735, 825, 4236, 3703, 2711, 530, 9630, 1521, 2174, 5027, 4833, 3483, 445, 8300, 3194, 8784,
            279, 3097, 1491, 9864, 4992, 6164, 2043, 5364, 9192, 9649, 9944, 7230, 7224, 585, 3722, 5628, 4833, 8379, 3967, 5649, 2554, 5828, 4331, 3547, 7847, 5433, 3394, 4968, 9983, 3540, 9224, 6216, 9665, 8070, 31, 3555, 4198, 2626, 9553, 9724, 4503, 1951, 9980, 3975, 6025, 8928, 2952, 911, 3674, 6620, 3745, 6548, 4985, 5206, 5777, 1908, 6029, 2322, 2626, 2188, 5639], 565610, 113)


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

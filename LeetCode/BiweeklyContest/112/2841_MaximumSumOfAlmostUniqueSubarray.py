from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = Counter(nums[:k])
        cur_sum = sum(nums[:k])
        best = 0

        if len(cnt) >= m:
            best = cur_sum

        for i in range(k, len(nums)):
            cnt[nums[i]] += 1
            cnt[nums[i-k]] -= 1
            if cnt[nums[i-k]] == 0:
                del cnt[nums[i-k]]
            cur_sum += nums[i] - nums[i-k]
            if len(cnt) >= m:
                best = max(best, cur_sum)

        return best


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.maxSum(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 6, 7, 3, 1, 7], 3, 4, 18)
    do_test(1, [5, 9, 9, 2, 4, 5, 4], 1, 3, 23)
    do_test(2, [1, 2, 1, 2, 1, 2, 1], 3, 3, 0)
    do_test(3, [1, 1, 2, 2], 1, 3, 5)
    do_test(4, [2, 4, 7, 9, 4, 9, 9, 9, 4], 3, 4, 29)


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

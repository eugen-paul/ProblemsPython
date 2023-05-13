from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


def rotate_90_degree_anticlckwise(matrix: List[List[int]]) -> List[List[int]]:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1, -1, -1)]


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        for i in range(len(nums)):
            nums[i].sort()

        nums = rotate_90_degree_anticlckwise(nums)

        return sum(map(max, nums))


def do_test(i: int, s, r):
    c = Solution()
    resp = c.matrixSum(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]], 15)


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

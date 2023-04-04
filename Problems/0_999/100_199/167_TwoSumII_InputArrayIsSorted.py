from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while True:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            if s > target:
                r -= 1
            else:
                l += 1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.twoSum(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 7, 11, 15], 9, [1, 2])
    do_test(1, [2, 3, 4], 6, [1, 3])
    do_test(2, [-1, 0], -1, [1, 2])

from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        s = set(nums[:k])
        if len(s) < len(nums[:k]):
            return True
        for i in range(k, len(nums)):
            s.add(nums[i])
            if len(s) != k+1:
                return True
            s.remove(nums[i-k])
        return False


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.containsNearbyDuplicate(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 1],  3, True)
    do_test(1, [1, 0, 1, 1],  1, True)
    do_test(2, [1, 2, 3, 1, 2, 3],  2, False)
    do_test(3, [99, 99],  2, True)

import bisect
from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class SegmentTree:

    # Max size of tree
    tree: List[int]
    source_array_len: int
    std_res = 0

    def __init__(self, arr: List[int]):
        self.source_array_len = len(arr)
        self.tree = [0] * (2 * self.source_array_len)

        # insert leaf nodes in tree
        for i in range(self.source_array_len):
            self.tree[self.source_array_len + i] = arr[i]

        # build the tree by calculating parents
        for i in range(self.source_array_len - 1, 0, -1):
            self.tree[i] = self._op(self.tree[i << 1], self.tree[i << 1 | 1])

    def _op(self, a: int, b: int) -> int:
        return a+b

    def updateTreeNode(self, p: int, value: int):
        # set value at position p
        self.tree[p + self.source_array_len] = value
        p = p + self.source_array_len

        # move upward and update parents
        i = p

        while i > 1:
            self.tree[i >> 1] = self._op(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l: int, r: int) -> int:
        res: int = self.std_res

        # loop to find the sum in the range
        l += self.source_array_len
        r += self.source_array_len + 1

        while l < r:
            if (l & 1):
                res = self._op(res, self.tree[l])
                l += 1

            if (r & 1):
                r -= 1
                res = self._op(res, self.tree[r])
            l >>= 1
            r >>= 1

        return res


class SegmentTreeMax (SegmentTree):
    std_res = -inf

    def _op(self, a, b) -> int:
        return max(a, b)


class Solution:

    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        s = list(set(obstacles))
        s.sort()
        ind = {v: i for i, v in enumerate(s)}

        tree = SegmentTreeMax([0]*len(s))

        resp = []

        for n in obstacles:
            v = ind[n]
            m = tree.query(0, v)
            tree.updateTreeNode(v, m+1)
            resp.append(m+1)

        return resp

    def longestObstacleCourseAtEachPosition_i(self, obstacles: List[int]) -> List[int]:
        """sample solution"""
        n = len(obstacles)
        answer = [1] * n

        # lis[i] records the lowest increasing sequence of length i + 1.
        lis = []

        for i, height in enumerate(obstacles):
            # Find the rightmost insertion position idx.
            idx = bisect.bisect_right(lis, height)

            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height
            answer[i] = idx + 1

        return answer


def do_test(i: int, s, r):
    c = Solution()
    resp = c.longestObstacleCourseAtEachPosition(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 2], [1, 2, 3, 3])
    do_test(1, [2, 2, 1], [1, 2, 1])
    do_test(2, [3, 1, 5, 6, 4, 2], [1, 1, 2, 3, 2, 2])
    do_test(3, [5, 1, 5, 5, 1, 3, 4, 5, 1, 4], [1, 1, 2, 3, 2, 3, 4, 5, 3, 5])
    do_test(4, [5, 4, 3, 2, 1, 5], [1, 1, 1, 1, 1, 2])

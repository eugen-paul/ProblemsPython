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
        """Contructor

        Args:
            arr (List[int]): array to convert to SegmentTree
        """

        self.source_array_len = len(arr)
        self.tree = [0] * (2 * self.source_array_len)

        # insert leaf nodes in tree
        for i in range(self.source_array_len):
            self.tree[self.source_array_len + i] = arr[i]

        # build the tree by calculating parents
        for i in range(self.source_array_len - 1, 0, -1):
            self.tree[i] = self._op(self.tree[i << 1], self.tree[i << 1 | 1])

    def _op(self, a: int, b: int) -> int:
        """operation to fill parent of nodes. override the op if you wand to get, max/min/sum/...\n
            !!! Don'n forgen to edit self.std_res !!!

        Args:
            a (int): value of one child
            b (int): value of other child

        Returns:
            int: response of operation
        """
        return a+b

    def updateTreeNode(self, p: int, value: int):
        """Update a tree node

        Args:
            p (int): index of node to update
            value (int): new value of the node
        """
        # set value at position p
        self.tree[p + self.source_array_len] = value
        p = p + self.source_array_len

        # move upward and update parents
        i = p

        while i > 1:
            self.tree[i >> 1] = self._op(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l: int, r: int) -> int:
        """function to get sum on interval [l, r]

        Args:
            l (int): from index inclusive
            r (int): to index inclusive

        Returns:
            int: sum
        """
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


class Solution:

    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        """using internet help"""
        a = [1 for _ in nums]
        seg = SegmentTree(a)

        s = [(n, i) for i, n in enumerate(nums)]
        s.sort()

        resp = 0
        pos = 0
        for _, i in s:
            if i >= pos:
                resp += seg.query(pos, i)
            else:
                resp += seg.query(pos, len(nums)-1)
                resp += seg.query(0, i)
            seg.updateTreeNode(i, 0)
            pos = i

        return resp

    def countOperationsToEmptyArray_1(self, nums: List[int]) -> int:
        """too slow"""
        s = sorted(nums)
        resp = 0
        while s:
            if nums[0] != s[0]:
                nums.append(nums.pop(0))
            else:
                s.pop(0)
                nums.pop(0)
            resp += 1
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.countOperationsToEmptyArray(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 4, -1], 5)
    do_test(1, [1, 2, 4, 3], 5)
    do_test(2, [1, 2, 3], 3)
    do_test(3, [-15, -19, 5], 5)

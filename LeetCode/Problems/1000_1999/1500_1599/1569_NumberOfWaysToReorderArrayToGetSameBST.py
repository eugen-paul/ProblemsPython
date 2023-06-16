from collections import defaultdict
from functools import cache
from math import comb, inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MOD = 10**9 + 7


class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        root = TreeNode(nums[0])

        def insert(node: TreeNode, val: int):
            if node.val > val:
                if node.left:
                    insert(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    insert(node.right, val)
                else:
                    node.right = TreeNode(val)

        for i in range(1, len(nums)):
            insert(root, nums[i])

        resp = 1

        def childs(node: TreeNode) -> int:
            if not node:
                return 0

            nonlocal resp
            left = childs(node.left)
            right = childs(node.right)
            resp = (resp * comb(left+right, left)) % MOD

            return left+right+1

        childs(root)
        return (resp-1) % MOD


def do_test(i: int, s, r):
    c = Solution()
    resp = c.numOfWays(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 1, 3], 1)
    do_test(1, [3, 4, 5, 1, 2], 5)
    do_test(2, [1, 2, 3], 0)

from math import inf
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = Deque()
        q.append((root, 1))
        resp = inf
        while q:
            cur, lev = q.pop()
            if lev >= resp:
                continue
            if cur.left is None and cur.right is None:
                resp = min(resp, lev)
            if cur.left:
                q.append((cur.left, lev+1))
            if cur.right:
                q.append((cur.right, lev+1))

        return resp

    def minDepth_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return 1+min(self.minDepth(root.left), self.minDepth(root.right))
        if root.left:
            return 1+self.minDepth(root.left)
        if root.right:
            return 1+self.minDepth(root.right)
        return 1

    def minDepth_1(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def get_depth(node: Optional[TreeNode], lev: int) -> int:
            if node.left is None and node.right is None:
                return lev

            return min(
                get_depth(node.left, lev+1) if node.left is not None else 10_000_000,
                get_depth(node.right, lev+1) if node.right is not None else 10_000_000,
            )

        return get_depth(root, 1)


def deserialize(string):
    if string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val)) for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    resp = list()

    def travel(node: Optional[TreeNode], level: int):
        if not node:
            return

        if len(resp) <= level:
            resp.append(list())

        travel(node.left, level + 1)
        resp[level].append(node.val)
        travel(node.right, level + 1)

    travel(root, 0)

    return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minDepth(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[3,9,20,null,null,15,7]", 2)
    do_test(1, "[2,null,3,null,4,null,5,null,6]", 5)
    do_test(2, "[]", 0)
    do_test(3, "[10]", 1)

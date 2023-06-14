from math import inf
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        q = Deque()
        q.append(root)
        last = inf
        resp = inf
        while q:
            node = q.pop()
            if not node:
                continue
            if node.left:
                q.append(node)
                q.append(node.left)
                node.left = None
            else:
                resp = min(resp, abs(last-node.val))
                last = node.val
                q.append(node.right)

        return resp

    def getMinimumDifference_1(self, root: Optional[TreeNode]) -> int:
        buf = []

        def walk(node):
            if not node:
                return
            buf.append(node.val)
            walk(node.left)
            walk(node.right)

        walk(root)
        buf.sort()
        resp = inf
        for i in range(1, len(buf)):
            resp = min(resp, buf[i]-buf[i-1])

        return resp


def deserialize(string: str):
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
    resp = c.getMinimumDifference(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[4,2,6,1,3]", 1)
    do_test(1, "[1,0,48,null,null,12,49]", 1)

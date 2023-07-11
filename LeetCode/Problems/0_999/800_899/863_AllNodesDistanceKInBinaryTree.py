from collections import defaultdict
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        m = defaultdict(set)
        q = Deque()
        q.append(root)

        while q:
            node = q.pop()
            if node.left:
                m[node.val].add(node.left.val)
                m[node.left.val].add(node.val)
                q.append(node.left)
            if node.right:
                m[node.val].add(node.right.val)
                m[node.right.val].add(node.val)
                q.append(node.right)

        q = Deque()
        q.append((target.val, -1, 0))

        resp = []
        while q:
            node, rt, lev = q.pop()
            if lev == k:
                resp.append(node)
            for nxt in m[node]:
                if nxt != rt:
                    q.append((nxt, node, lev+1))
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


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.distanceK(deserialize(s), n, k)
    if sorted(resp) == sorted(r):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[3,5,1,6,2,0,8,null,null,7,4]", TreeNode(5), 2, [7, 4, 1])
    do_test(1, "[1]", TreeNode(1), 3, [])
    do_test(2, "[3,5,1,6,2,0,8,null,null,7,4]", TreeNode(2), 1, [7, 4, 5])

from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        return right


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
    resp = c.lowestCommonAncestor(deserialize(s), TreeNode(n), TreeNode(k))
    if resp.val == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp.val)


if __name__ == "__main__":
    do_test(0, "[3,5,1,6,2,0,8,null,null,7,4]", 5, 1, 3)
    do_test(1, "[3,5,1,6,2,0,8,null,null,7,4]", 5, 4, 5)
    do_test(2, "[3,5,1,6,2,0,8,null,null,7,4]", 3, 1, 3)
    do_test(3, "[1,2]", 1, 2, 1)

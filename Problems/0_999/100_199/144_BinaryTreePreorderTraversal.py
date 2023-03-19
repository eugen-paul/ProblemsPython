from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resp = []
        to_check = Deque()
        to_check.append(root)

        while to_check:
            node = to_check.popleft()
            if not node:
                continue

            resp.append(node.val)
            to_check.appendleft(node.right)
            to_check.appendleft(node.left)

        return resp

    def preorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        resp = []

        def travel(node: Optional[TreeNode]):
            if not node:
                return
            resp.append(node.val)
            travel(node.left)
            travel(node.right)

        travel(root)
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
    resp = c.preorderTraversal(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[1,null,2,3]", [1, 2, 3])
    do_test(1, "[]", [])
    do_test(2, "[1]", [1])

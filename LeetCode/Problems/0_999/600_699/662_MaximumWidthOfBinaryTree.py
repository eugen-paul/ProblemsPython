from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [root]
        root.val = 1
        resp = 1

        while q:
            resp = max(resp, q[-1].val - q[0].val + 1)
            nxt = []
            for node in q:
                if node.left:
                    node.left.val = node.val * 2
                    nxt.append(node.left)
                if node.right:
                    node.right.val = node.val * 2 + 1
                    nxt.append(node.right)
            q = nxt

        return resp

    def widthOfBinaryTree_2(self, root: Optional[TreeNode]) -> int:
        mm: List[int] = []
        resp: int = 1

        def rec(node: Optional[TreeNode], v: int, level: int):
            if not node:
                return
            if len(mm) == level:
                mm.append(v)
            else:
                nonlocal resp
                resp = max(resp, v-mm[level]+1)

            rec(node.left, v * 2, level+1)
            rec(node.right, v * 2+1, level+1)

        rec(root, 1, 0)

        return resp

    def widthOfBinaryTree_1(self, root: Optional[TreeNode]) -> int:

        mm: List[Tuple[int, int]] = []

        def rec(node: Optional[TreeNode], v: int, level: int):
            if not node:
                return
            if len(mm) == level:
                mm.append((v, v))
            else:
                mm[level] = (mm[level][0], v)

            rec(node.left, v * 2, level+1)
            rec(node.right, v * 2+1, level+1)

        rec(root, 1, 0)
        resp = 0
        for mi, ma in mm:
            resp = max(resp, ma-mi+1)

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
    resp = c.widthOfBinaryTree(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[1,3,2,5,3,null,9]", 4)
    do_test(1, "[1,3,2,5,null,null,9,6,null,7]", 7)
    do_test(2, "[1,3,2,5]", 2)
    do_test(3, "[1]", 1)

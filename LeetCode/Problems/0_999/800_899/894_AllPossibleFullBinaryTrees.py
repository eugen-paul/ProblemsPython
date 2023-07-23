from functools import cache
from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def solve(n: int) -> List[Optional[TreeNode]]:
            if n == 1:
                return [TreeNode(0)]

            resp = []

            for i in range(1, n, 2):
                left = solve(i)
                right = solve(n-i-1)
                for l in left:
                    for r in right:
                        cur = TreeNode(0, left=l, right=r)
                        resp.append(cur)
            return resp

        return solve(n)


def deserialize(string: str):
    if string == '[]':
        return None
    nodes = [None if val == 'None' else TreeNode(int(val)) for val in string.strip('[]{}').split(',')]
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
    resp = c.allPossibleFBT(s)
    
    if isSameTree(resp, deserialize(r)):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response")


if __name__ == "__main__":
    do_test(0, 7,
            [
                [0, 0, 0, None, None, 0, 0, None, None, 0, 0],
                [0, 0, 0, None, None, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, None, None, None, None, 0, 0],
                [0, 0, 0, 0, 0, None, None, 0, 0]
            ]
            )
    do_test(1, 3,
            [[0, 0, 0]]
            )

from math import inf
from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []

        def comp(node: Optional[TreeNode], lvl: int):
            if not node:
                return
            if len(sums) < lvl:
                sums.append(node.val)
            else:
                sums[lvl-1] += node.val
            comp(node.left, lvl+1)
            comp(node.right, lvl+1)
        comp(root, 1)

        mi = -inf
        resp = 0
        for i, n in enumerate(sums):
            if mi < n:
                resp = i
                mi = n
        return resp+1


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
    resp = c.maxLevelSum(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[1,7,0,7,-8,null,null]", 2)
    do_test(1, "[989,null,10250,98693,-89388,null,null,null,-32127]", 2)

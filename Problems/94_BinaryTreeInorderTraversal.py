# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return list()

        resp = list()

        if root.left:
            resp.extend(self.inorderTraversal(root.left))
        resp.append(root.val)
        if root.right:
            resp.extend(self.inorderTraversal(root.right))
        return resp

##########################################
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def do_test(i: int, s, r):
    c = Solution()
    resp = c.inorderTraversal(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[1,null,2,3]", [1, 3, 2])
    do_test(1, "[]", [])
    do_test(2, "[1]", [1])
    do_test(3, "[1,10,2,3,null,4,5,6,7,null,null,null,8,11,12,13,14,15,16]", [11,6,12,3,13,7,14,10,1,4,2,5,15,8,16])

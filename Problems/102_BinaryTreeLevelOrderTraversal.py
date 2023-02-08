from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

    def levelOrder_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        resp = Deque()

        def travel(node: Optional[TreeNode], level: int):
            if not node:
                return

            if len(resp) <= level:
                resp.append(Deque())

            travel(node.left, level + 1)
            resp[level].append(node.val)
            travel(node.right, level + 1)

        travel(root, 0)

        return resp


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
    resp = c.levelOrder(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[3,9,20,null,null,15,7]", [[3], [9, 20], [15, 7]])
    do_test(1, "[1]", [[1]])
    do_test(2, "[]", [])

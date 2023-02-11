from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resp: List[List[int]] = list()

        def to_list(node: Optional[TreeNode], level: int):
            if node is None:
                return
            if len(resp) <= level:
                resp.append(list())
            resp[level].append(node.val)
            to_list(node.left, level+1)
            to_list(node.right, level+1)

        to_list(root, 0)

        for i in range(len(resp)):
            if i % 2 == 1:
                resp[i].reverse()

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
    resp = c.zigzagLevelOrder(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[3,9,20,null,null,15,7]", [[3], [20, 9], [15, 7]])
    do_test(1, "[1]", [[1]])
    do_test(2, "[]", [])

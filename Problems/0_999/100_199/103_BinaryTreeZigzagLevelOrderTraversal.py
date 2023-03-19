from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resp = list()

        to_check = Deque()
        to_check.append((root,0))

        while to_check:
            node,lev = to_check.pop()
            if not node:
                continue
            if len(resp) <= lev:
                resp.append(list())
            resp[lev].append(node.val)
            to_check.append((node.left,lev+1))
            to_check.append((node.right,lev+1))

        for i,q in enumerate(resp):
            if i % 2 == 0:
                q.reverse()
        return resp
    
    def zigzagLevelOrder_1(self, root: Optional[TreeNode]) -> List[List[int]]:
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

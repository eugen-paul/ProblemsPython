from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        max_lev = None
        edit = False

        def travel(node: Optional[TreeNode], cur_level: int) -> bool:
            nonlocal max_lev
            nonlocal edit

            if not node:
                if max_lev is None:
                    max_lev = cur_level
                    return True
                if max_lev == cur_level:
                    return True
                if max_lev-1 == cur_level and not edit:
                    max_lev = cur_level
                    edit = True
                    return True
                return False

            return travel(node.left, cur_level+1) and travel(node.right, cur_level+1)

        return travel(root, 0)


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
    resp = c.isCompleteTree(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[1,2,3,4,5,6]", True)
    do_test(1, "[1,2,3,4,5,null,7]", False)
    do_test(2, "[1]", True)
    do_test(3, "[1,null,2]", False)
    do_test(4, "[1,2,3,4,5]", True)
    do_test(5, "[1,2,3,4]", True)
    do_test(6, "[1,2,3,4,5,6,null,8]", False)
    do_test(7, "[1,2,3,null,null,6,7]", False)

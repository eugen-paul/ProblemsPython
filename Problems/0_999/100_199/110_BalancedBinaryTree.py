from typing import Deque, List, Optional, Tuple


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_depth(node: Optional[TreeNode], cur_depth: int) -> Tuple[bool, int]:
            if node is None:
                return (True, cur_depth)

            l = get_depth(node.left, cur_depth+1)
            r = get_depth(node.right, cur_depth+1)
            if l[0] and r[0] and abs(l[1]-r[1]) <= 1:
                return (True, max(l[1], r[1]))
            return (False, max(l[1], r[1]))

        return get_depth(root, 0)[0]


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
    resp = c.isBalanced(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[3,9,20,null,null,15,7]", True)
    do_test(1, "[1,2,2,3,3,null,null,4,4]", False)
    do_test(2, "[]", True)
    do_test(3, "[1,2,3,4,5,6,null,8]", True)

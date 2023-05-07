from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.val = 0
        cur_level_sum = 0
        cur_level = [root]

        nxt_lev_sum = 0
        nxt_lev = []
        while cur_level:
            node = cur_level.pop()
            node.val = cur_level_sum - node.val
            if node.left:
                nxt_lev_sum += node.left.val
                nxt_lev.append(node.left)
            if node.right:
                nxt_lev_sum += node.right.val
                nxt_lev.append(node.right)
            if node.left and node.right:
                v = node.left.val + node.right.val
                node.left.val, node.right.val = v, v

            if len(cur_level) == 0:
                cur_level_sum = nxt_lev_sum
                cur_level = nxt_lev
                nxt_lev_sum = 0
                nxt_lev = []

        return root

    def replaceValueInTree_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.val = 0

        cur_level_sum = 0
        cur_level = []

        if root.left:
            cur_level_sum = root.left.val
            cur_level.append(root.left)
        if root.right:
            cur_level_sum += root.right.val
            cur_level.append(root.right)

        if root.left and root.right:
            v = root.left.val + root.right.val
            root.left.val, root.right.val = v, v

        nxt_lev_sum = 0
        nxt_lev = []
        while cur_level:
            node = cur_level.pop()
            node.val = cur_level_sum - node.val
            if node.left:
                nxt_lev_sum += node.left.val
                nxt_lev.append(node.left)
            if node.right:
                nxt_lev_sum += node.right.val
                nxt_lev.append(node.right)
            if node.left and node.right:
                v = node.left.val + node.right.val
                node.left.val, node.right.val = v, v

            if len(cur_level) == 0:
                cur_level_sum = nxt_lev_sum
                cur_level = nxt_lev
                nxt_lev_sum = 0
                nxt_lev = []

        return root


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
    resp = c.replaceValueInTree(deserialize(s))
    r = deserialize(r)
    if isSameTree(r, resp):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[5,4,9,1,10,null,7]", "[0,0,0,7,7,null,11]")
    do_test(1, "[3,1,2]", "[0,0,0]")

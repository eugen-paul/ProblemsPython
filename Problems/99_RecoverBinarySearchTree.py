from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        to_check = Deque()
        to_check.append((root, None, None))

        while to_check:
            node, min_root, max_root = to_check.pop()
            if node.left and (node.val <= node.left.val or (min_root and min_root >= node.left.val)):
                node.left.val, node.val = node.val, node.left.val
                to_check.clear()
                to_check.append((root, None, None))
            elif node.right and (node.val >= node.right.val or (max_root and max_root <= node.right.val)):
                node.right.val, node.val = node.val, node.right.val
                to_check.clear()
                to_check.append((root, None, None))
            else:
                if node.left:
                    to_check.append((
                        node.left,
                        min(node.val, min_root) if min_root else None,
                        min(node.val, max_root) if max_root else node.val,
                    ))
                if node.right:
                    to_check.append((
                        node.right,
                        max(node.val, min_root) if min_root else node.val,
                        max(node.val, max_root) if max_root else None
                    ))


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
    resp = c.recoverTree(deserialize(s))
    # if resp == r:
    #     print("OK", i)
    # else:
    #     print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, "[1,3,null,null,2]", "[3,1,null,null,2]")
    do_test(1, "[3,1,4,null,null,2]", "[2,1,4,null,null,3]")

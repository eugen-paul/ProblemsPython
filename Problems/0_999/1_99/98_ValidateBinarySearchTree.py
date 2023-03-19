from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        to_check = Deque()
        to_check.append((root, None, None))

        while to_check:
            node, min_root, max_root = to_check.pop()
            if not node:
                continue
            if node.left:
                if node.val <= node.left.val or (min_root and min_root >= node.left.val):
                    return False
                to_check.append((node.left, min_root, node.val))
            if node.right:
                if node.val >= node.right.val or (max_root and max_root <= node.right.val):
                    return False
                to_check.append((node.right, node.val, max_root))

        return True

    def isValidBST_2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        to_check = Deque()
        to_check.append((root, None, None))

        while to_check:
            node, min_root, max_root = to_check.pop()
            if not node:
                continue
            if node.left:
                if node.val <= node.left.val or (min_root and min_root >= node.left.val):
                    return False
                to_check.append((
                    node.left,
                    min(node.val, min_root) if min_root else None,
                    min(node.val, max_root) if max_root else node.val,
                ))
            if node.right:
                if node.val >= node.right.val or (max_root and max_root <= node.right.val):
                    return False
                to_check.append((
                    node.right,
                    max(node.val, min_root) if min_root else node.val,
                    max(node.val, max_root) if max_root else None
                ))

        return True


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
    resp = c.isValidBST(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[2,1,3]", True)
    do_test(1, "[5,1,4,null,null,3,6]", False)
    do_test(2, "[5,4,6,null,null,3,7]", False)
    do_test(3, "[32,26,47,19,null,null,56,null,27]", False)
    do_test(4, "[-80,null,38,25,null,-43]", True)

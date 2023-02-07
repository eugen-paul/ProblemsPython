from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        sorted = Deque()

        def add_to_sorted(node: Optional[TreeNode]):
            if not node:
                return
            add_to_sorted(node.left)
            sorted.append(node)
            add_to_sorted(node.right)

        add_to_sorted(root)

        a = sorted[0]
        for cur in sorted:
            if a.val > cur.val:
                break
            a = cur

        b = sorted[-1]
        for cur in reversed(sorted):
            if b.val < cur.val:
                break
            b = cur

        a.val, b.val = b.val, a.val

    def recoverTree_1(self, root: Optional[TreeNode]) -> None:

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
                    to_check.append((node.left, min_root, node.val))
                if node.right:
                    to_check.append((node.right, node.val, max_root))

    def recoverTree_inet(self, root: Optional[TreeNode]) -> None:
        """
        Internet solution
        """
        curr, prev, a, b = root, None, None, None
        while curr:
            if not curr.left:
                # find the node that is violating the ordering
                if prev and curr.val < prev.val:
                    if not a:  # find the first node to swap
                        a = prev
                    b = curr
                prev = curr
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right is not curr:
                    temp = temp.right
                if temp.right is curr:
                    temp.right = None
                    if prev and curr.val < prev.val:
                        if not a:
                            a = prev
                        b = curr
                    prev = curr
                    curr = curr.right
                else:
                    temp.right = curr
                    curr = curr.left

                # swap bide values
        a.val, b.val = b.val, a.val


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

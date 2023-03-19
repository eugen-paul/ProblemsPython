from typing import Deque, List, Optional, Tuple


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def compute_node(sub_io: List[int]) -> Optional[TreeNode]:
            if len(preorder) == 0 or len(sub_io) == 0:
                return None

            node = TreeNode(preorder.pop(0))
            pos_left = sub_io.index(node.val)
            node.left = compute_node(sub_io[:pos_left])
            node.right = compute_node(sub_io[pos_left+1:])

            return node

        return compute_node(inorder)

    def buildTree_1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        resp = TreeNode(preorder[0])

        def set_childs(node: TreeNode, in_left: List[int], in_right: List[int]) -> Optional[TreeNode]:
            if len(preorder) == 0:
                return

            try:
                pos_left = in_left.index(preorder[0])
                node.left = TreeNode(preorder[0])
                preorder.pop(0)
                set_childs(node.left, in_left[:pos_left], in_left[pos_left+1:])
            except ValueError:
                pass

            if len(preorder) > 0:
                try:
                    pos_right = in_right.index(preorder[0])
                    node.right = TreeNode(preorder[0])
                    preorder.pop(0)
                    set_childs(node.right, in_right[:pos_right], in_right[pos_right+1:])
                except ValueError:
                    pass

            pass

        pos = inorder.index(preorder[0])
        preorder.pop(0)
        set_childs(resp, inorder[:pos], inorder[pos+1:])

        return resp


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


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


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.buildTree(s, n)
    if isSameTree(resp, deserialize(r)):
        print("OK", i)
    else:
        print("NOK", i, "expected", levelOrder(deserialize(r)), "response", levelOrder(resp))


if __name__ == "__main__":
    do_test(0, [3, 9, 20, 15, 7], [9, 3, 15, 20, 7], "[3,9,20,null,null,15,7]")
    do_test(1, [-1], [-1], "[-1]")
    do_test(2, [3, 1, 2, 4], [1, 2, 3, 4], "[3,1,4,null,2]")

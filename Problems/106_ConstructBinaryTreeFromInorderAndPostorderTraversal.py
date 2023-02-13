from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        m = {n: i for i, n in enumerate(inorder)}

        def comp_node(from_inorder: int, to_inorder: int, from_postorder: int, to_postorder: int) -> Optional[TreeNode]:
            if from_inorder > to_inorder:
                return None

            root = TreeNode(postorder[to_postorder])
            pos = m.get(postorder[to_postorder])
            root.left = comp_node(from_inorder, pos - 1, from_postorder, from_postorder + ((pos -1) - from_inorder))
            root.right = comp_node(pos + 1, to_inorder, to_postorder - 1 - (to_inorder - (pos + 1)), to_postorder - 1)

            return root

        r = comp_node(0, len(inorder)-1, 0, len(postorder)-1)
        return r

    def buildTree_1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def comp_node(sub_inorder: List[int], sub_postorder: List[int]) -> Optional[TreeNode]:
            if len(sub_inorder) == 0:
                return None
            root = TreeNode(sub_postorder[-1])
            pos = sub_inorder.index(sub_postorder[-1])
            root.left = comp_node(sub_inorder[:pos], sub_postorder[:pos])
            root.right = comp_node(sub_inorder[pos+1:], sub_postorder[pos:-1])

            return root

        r = comp_node(inorder, postorder)
        return r


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


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.buildTree(s, n)
    if isSameTree(resp, deserialize(r)):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", levelOrder(resp))


if __name__ == "__main__":
    do_test(0, [9, 3, 15, 20, 7], [9, 15, 7, 20, 3], "[3,9,20,null,null,15,7]")
    do_test(1, [-1], [-1], "-1")

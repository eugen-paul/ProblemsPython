from typing import Counter, Dict, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        m = dict()
        resp = set()
        trees = Counter()

        def hash(node: Optional[TreeNode]) -> str:
            if not node:
                return "-"
            if id(node) in m:
                return m[id(node)]
            h = "v"+str(node.val)+"l"+hash(node.left)+"r"+hash(node.right)+":"
            m[id(node)] = h
            return h

        def check_node(node: Optional[TreeNode]):
            if not node:
                return
            h = hash(node)
            if trees.get(h, 0) == 1:
                resp.add(node)
            trees[h] += 1
            check_node(node.left)
            check_node(node.right)

        check_node(root)

        return [a for a in resp]

    def findDuplicateSubtrees_1(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        resp = set()
        trees = Counter()

        def hash(node: Optional[TreeNode]) -> str:
            if not node:
                return "-"
            h = "v"+str(node.val)+"l"+hash(node.left)+"r"+hash(node.right)+":"
            return h

        def check_node(node: Optional[TreeNode]):
            if not node:
                return
            h = hash(node)
            if trees.get(h, 0) == 1:
                resp.add(node)
            trees[h] += 1
            check_node(node.left)
            check_node(node.right)

        check_node(root)

        return [a for a in resp]


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
    c.findDuplicateSubtrees(deserialize(s))


if __name__ == "__main__":
    do_test(0, "[1,2,3,4,null,2,4,null,null,4]", [[2, 4], 4])
    do_test(1, "[2,1,1]", [[1]])
    do_test(2, "[2,2,2,3,null,3,null]", [[2, 3], [3]])

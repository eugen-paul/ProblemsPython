from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        resp = list()

        to_check = Deque()
        to_check.append((root, [], 0))

        while to_check:
            node, path, s = to_check.pop()
            if node is None:
                continue
            s += node.val

            if node.left is None and node.right is None and s == targetSum:
                resp.append(path + [node.val])
                continue

            to_check.append((node.left, [*path] + [node.val], s))
            to_check.append((node.right, path + [node.val], s))

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
    resp = c.pathSum(deserialize(s), n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[5,4,8,11,null,13,4,7,2,null,null,5,1]", 22, [[5, 4, 11, 2], [5, 8, 4, 5]])
    do_test(1, "[1,2,3]", 5, [])
    do_test(2, "[1,2]", 0, [])
    do_test(3, "[]", 0, [])

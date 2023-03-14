from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        resp = 0

        def walk(node: Optional[TreeNode], path: List[str]):
            nonlocal resp
            if not node:
                return
            if not node.left and not node.right:
                resp += int("".join(path)) * 10 + node.val
                return

            walk(node.left, path + [str(node.val)])
            walk(node.right, path + [str(node.val)])

        walk(root, [str(0)])

        return resp

    def sumNumbers_1(self, root: Optional[TreeNode]) -> int:
        resp = 0

        to_check: Deque[TreeNode, str] = Deque()
        to_check.append((root, ""))

        while to_check:
            node, path = to_check.pop()
            if not node:
                continue
            if not node.left and not node.right:
                resp += int(path + str(node.val))
                continue

            to_check.append((node.left, path + str(node.val)))
            to_check.append((node.right, path + str(node.val)))

        return resp


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
    resp = c.sumNumbers(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[1,2,3]", 25)
    do_test(1, "[4,9,0,5,1]", 1026)
    do_test(2, "[0]", 0)

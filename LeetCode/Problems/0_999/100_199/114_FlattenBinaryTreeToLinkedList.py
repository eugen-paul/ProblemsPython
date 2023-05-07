from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        q = Deque()
        q.append(root)
        last = TreeNode(-1)

        while q:
            node = q.popleft()
            if not node:
                continue
            last.right = node
            last = node
            q.appendleft(node.right)
            q.appendleft(node.left)
            node.left = None
            node.right = None

    def flatten_1(self, root: Optional[TreeNode]) -> None:
        self.last = TreeNode(-1)

        def flatt(node: Optional[TreeNode]):
            if not node:
                return
            self.last.right = node
            self.last = node
            l = node.left
            r = node.right
            node.left = None
            node.right = None
            flatt(l)
            flatt(r)

        flatt(root)


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
    s = deserialize(s)
    c.flatten(s)
    if isSameTree(s, deserialize(r)):
        print("OK", i)
    else:
        print("NOK", i, "expected", levelOrder(deserialize(r)), "response", levelOrder(s))


if __name__ == "__main__":
    do_test(0, "[1,2,5,3,4,null,6]", "[1,null,2,null,3,null,4,null,5,null,6]")
    do_test(1, "[1]", "[1]")
    do_test(2, "[]", "[]")

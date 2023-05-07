from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        resp = []
        q = Deque()
        q.append((root, 0))

        while q:
            n, lev = q.popleft()
            if not n:
                continue
            if len(resp) <= lev:
                resp.append(n.val)
            else:
                resp[lev] = n.val
            q.append((n.left, lev+1))
            q.append((n.right, lev+1))

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
    resp = c.rightSideView(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[1,2,3,null,5,null,4]", [1, 3, 4])
    do_test(1, "[1,null,3]", [1, 3])
    do_test(2, "[]", [])
    do_test(3, "[1,2,3,null,5,null,4,9]", [1, 3, 4, 9])

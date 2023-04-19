from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        best = 0

        # left true
        # right false
        def walk(node: Optional[TreeNode], way: List[bool]):
            if not node:
                return

            nonlocal best

            best = max(best, len(way))

            if way[-1]:
                walk(node.left, [True])
                way.append(False)
                walk(node.right, way)
                way.pop()
            else:
                way.append(True)
                walk(node.left, way)
                way.pop()
                walk(node.right, [False])

        walk(root.left, [True])
        walk(root.right, [False])
        return best


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
    resp = c.longestZigZag(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]", 3)
    do_test(1, "[1,1,1,null,1,null,null,1,1,null,1]", 4)
    do_test(2, "[1]", 0)

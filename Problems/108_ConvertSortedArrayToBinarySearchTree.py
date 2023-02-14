from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def create_node(nums: List[int]) -> Optional[TreeNode]:
            if len(nums) == 0:
                return None

            n = TreeNode(nums[len(nums) // 2])
            n.left = create_node(nums[:len(nums) // 2])
            n.right = create_node(nums[len(nums) // 2 + 1:])
            return n

        return create_node(nums)


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
    resp = c.sortedArrayToBST(s)
    if isSameTree(resp, deserialize(r)):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", levelOrder(resp))


if __name__ == "__main__":
    do_test(0, [-10, -3, 0, 5, 9], "[0,-3,9,-10,null,5]")

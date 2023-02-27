from typing import List, Dict, Optional, Tuple, Counter


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# --------------------------


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return None


def isSameTree(p: Optional[Node], q: Optional[Node]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.isLeaf != q.isLeaf:
        return False
    if p.isLeaf and q.isLeaf and p.val != q.val:
        return False
    return isSameTree(p.topLeft, q.topLeft) \
        and isSameTree(p.topRight, q.topRight) \
        and isSameTree(p.bottomLeft, q.bottomLeft) \
        and isSameTree(p.bottomRight, q.bottomRight)


def deserialize(string: str) -> Node:
    nodes = [None if val == 'null' else Node(int(val[2]), val[0] == '1', None, None, None, None)
             for val in string.strip('[]{}').replace("null", "[null]").split('],[')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.topLeft = kids.pop()
            if kids:
                node.topRight = kids.pop()
            if kids:
                node.bottomLeft = kids.pop()
            if kids:
                node.bottomRight = kids.pop()

    return root


def do_test(i: int, s, r):
    c = Solution()
    resp = c.construct(s)
    if isSameTree(resp, deserialize(r)):
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 42, "[[0,1],[1,0],[1,1],[1,1],[1,0]]")

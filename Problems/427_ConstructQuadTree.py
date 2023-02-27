from typing import List, Optional


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def is_same_values(self, grid: List[List[int]]) -> bool:
        a = grid[0][0]
        for r in grid:
            for e in r:
                if a != e:
                    return False
        return True

    def parts(self, grid: List[List[int]]) -> List[List[List[int]]]:
        a, b, c, d = [], [], [], []
        resp = [a, b, c, d]
        for r in range(len(grid)):
            k = 0
            if r >= len(grid) // 2:
                k = 2
            row = []
            for c in range(len(grid[0])):
                if c == len(grid[0]) // 2:
                    resp[k].append(row)
                    row = []
                    k += 1
                row.append(grid[r][c])
            resp[k].append(row)
        return resp

    def construct(self, grid: List[List[int]]) -> 'Node':
        if self.is_same_values(grid):
            resp = Node(
                grid[0][0],
                True,
                None, None, None, None
            )
            return resp

        parts: List[List[List[int]]] = self.parts(grid)
        resp = Node(
            None,
            False,
            self.construct(parts[0]),
            self.construct(parts[1]),
            self.construct(parts[2]),
            self.construct(parts[3]),
        )
        return resp


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
    do_test(0, [[0, 1], [1, 0]], "[[0,1],[1,0],[1,1],[1,1],[1,0]]")
    do_test(1, [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0]
    ], "[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]")

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.buffer = []
        self.cur = root

        self.nxt = True
        while self.cur:
            self.buffer.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.buffer.pop()

    def next(self) -> int:
        resp = self.cur.val

        if self.cur.right:
            self.cur = self.cur.right
            while self.cur:
                self.buffer.append(self.cur)
                self.cur = self.cur.left
            self.cur = self.buffer.pop()
        else:
            if self.buffer:
                self.cur = self.buffer.pop()
            else:
                self.nxt = False

        return resp

    def hasNext(self) -> bool:
        return self.nxt


def do_test(j: int, s, n, r):
    it = None

    for i, c in enumerate(s):
        if c == "BSTIterator":
            it = BSTIterator(deserialize(n[i]))
        elif c == "next":
            q = it.next()
            if q != r[i]:
                print("next Error!", i)
        elif c == "hasNext":
            q = it.hasNext()
            if q != r[i]:
                print("hasNext Error!", i)


if __name__ == "__main__":
    do_test(0, ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
            ["[7,3,15,null,null,9,20]", [], [], [], [], [], [], [], [], []],
            [None, 3, 7, True, 9, True, 15, True, 20, False]
            )

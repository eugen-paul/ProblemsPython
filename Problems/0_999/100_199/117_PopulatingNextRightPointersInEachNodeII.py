from typing import Deque, List, Optional, Tuple


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def set_next(node: 'Node'):
            if not node:
                return

            if node.left and node.right:
                node.left.next = node.right

            if node.left or node.right and node.next:
                child = node.right if node.right else node.left
                nn = node.next
                while nn and (not nn.left and not nn.right):
                    nn = nn.next
                if nn:
                    child.next = nn.left if nn.left else nn.right

            set_next(node.right)
            set_next(node.left)

        set_next(root)
        return root

    def connect_1(self, root: 'Node') -> 'Node':
        if not root:
            return root
        to_check: Deque[Tuple[Node, int]] = Deque()
        to_check.append((root, 0))

        while to_check:
            node, level = to_check.popleft()
            if to_check and to_check[0][1] == level:
                node.next = to_check[0][0]
            if node.left:
                to_check.append((node.left, level+1))
            if node.right:
                to_check.append((node.right, level+1))

        return root


def do_test(i: int, s, r):
    c = Solution()
    resp = c.connect(deserialize(s))
    # if resp == r:
    #     print("OK", i)
    # else:
    #     print("NOK", i, "expected", r, "response", resp)


def deserialize(string):
    if string == '[]':
        return None
    nodes = [None if val == 'null' else Node(int(val)) for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


if __name__ == "__main__":
    do_test(0, "[1,2,3,4,5,null,7]", "[1,#,2,3,#,4,5,7,#]")
    do_test(1, "[1,2,3,4,null,null,5]", "[1,#,2,3,#,4,5,#]")

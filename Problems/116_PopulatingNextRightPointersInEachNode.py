from typing import List, Dict, Optional, Tuple, Counter


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def get_last(prev_node: 'Optional[Node]', node: 'Optional[Node]', next_node: 'Optional[Node]') -> 'Optional[Node]':
            if not node:
                return None

            if not prev_node and not next_node:
                get_last(None, node.left, node.right)
                get_last(node.left, node.right, None)
            elif not prev_node:
                node.next = next_node
                get_last(None, node.left, node.right)
                get_last(node.left, node.right, next_node.left)
            elif not next_node:
                prev_node.next = node
                get_last(prev_node.right, node.left, node.right)
                get_last(node.left, node.right, None)
            else:
                prev_node.next = node
                node.next = next_node
                get_last(prev_node.right, node.left, node.right)
                get_last(node.left, node.right, next_node.left)

            return node.right

        get_last(None, root, None)

        return root


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


def do_test(i: int, s, r):
    c = Solution()
    resp = c.connect(deserialize(s))
    # if resp == r:
    #     print("OK", i)
    # else:
    #     print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[1,2,3,4,5,6,7]", "[1,#,2,3,#,4,5,6,7,#]")

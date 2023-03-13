from copy import deepcopy
from typing import Dict, List, Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# -------------------

        pass


def from_list(data: Node) -> List[List[int]]:
    response = []
    order: Dict[Node, int] = dict()

    pos = 0
    cur = data
    while cur != None:
        order[cur] = pos
        pos += 1
        cur = cur.next

    cur = data
    while cur != None:
        response.append([cur.val, order.get(cur.random, None)])
        cur = cur.next
    return response


def gen_list(data: list) -> Node:
    order: List[Node] = [Node(d[0]) for d in data]

    resp = Node(-1)
    last = resp
    for i, d in enumerate(data):
        cur = order[i]
        cur.random = order[d[1]] if d[1] is not None else None
        last.next = cur
        last = cur
    return resp.next


def do_test(i: int, s, r):
    c = Solution()
    resp = c.copyRandomList(gen_list(s))
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]], [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])

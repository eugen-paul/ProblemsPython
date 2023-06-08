from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next


def from_list(data: ListNode) -> List[int]:
    response = []
    cur = data
    while cur != None:
        response.append(cur.val)
        cur = cur.next
    return response


def gen_list(data: list) -> ListNode:
    last = None
    for x in reversed(data):
        cur = ListNode(x, last)
        last = cur
    return last


def do_test(i: int, s, n, r):
    c = Solution()

    inp = gen_list(s)
    cur = inp
    while cur.val != n:
        cur = cur.next

    c.deleteNode(cur)
    if from_list(inp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(s))


if __name__ == "__main__":
    do_test(0, [4, 5, 1, 9], 5, [4, 1, 9])
    do_test(1, [4, 5, 1, 9], 1, [4, 5, 9])

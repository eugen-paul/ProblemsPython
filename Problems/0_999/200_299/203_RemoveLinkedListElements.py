from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        resp = ListNode()
        last = resp
        while head:
            nxt = head.next
            head.next = None
            if head.val != val:
                last.next = head
                last = head
            head = nxt

        return resp.next


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
    resp = c.removeElements(gen_list(s), n)
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5])
    do_test(1, [], 1, [])
    do_test(2, [7, 7, 7, 7], 7, [])

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resp = ListNode(-10_000)

        while head:
            nxt = head.next

            curr = resp
            while curr.next and curr.next.val < head.val:
                curr = curr.next

            head.next = curr.next
            curr.next = head

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


def do_test(i: int, s, r):
    c = Solution()
    resp = c.insertionSortList(gen_list(s))
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [4, 2, 1, 3], [1, 2, 3, 4])
    do_test(1, [-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])
    do_test(2, [1, 2], [1, 2])
    do_test(3, [1], [1])

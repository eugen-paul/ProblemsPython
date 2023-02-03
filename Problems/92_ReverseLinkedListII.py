##########################################
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        resp = ListNode(0)
        cur = resp
        rev = []

        for i in range(1, right+1):
            if i < left:
                cur.next = head
                cur = cur.next
            if i >= left and i <= right:
                rev.append(head.val)
            head = head.next

        for n in reversed(rev):
            cur.next = ListNode(n)
            cur = cur.next
        cur.next = head
        return resp.next

    def reverseBetween_2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = []
        rev = []
        end = []

        state = 0
        i = 1
        while head:
            if i >= left and i <= right:
                state = 1
            elif i > right:
                state = 2

            if state == 0:
                start.append(head.val)
            elif state == 1:
                rev.append(head.val)
            else:
                end.append(head.val)
            head = head.next
            i += 1

        resp = ListNode(0)
        cur = resp

        for n in start:
            cur.next = ListNode(n)
            cur = cur.next
        for n in reversed(rev):
            cur.next = ListNode(n)
            cur = cur.next
        for n in end:
            cur.next = ListNode(n)
            cur = cur.next
        return resp.next

    def reverseBetween_1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = ListNode(0)
        start_end = start

        rev = None
        rev_end = None

        end = ListNode(0)
        end_end = end

        state = 0
        i = 1
        while head:
            if i >= left and i <= right:
                state = 1
            elif i > right:
                state = 2

            if state == 0:
                start_end.next = head
                head = head.next
                start_end = start_end.next
                start_end.next = None
            elif state == 1:
                cur = head
                head = head.next
                cur.next = rev
                rev = cur
                if rev_end == None:
                    rev_end = rev
            else:
                end_end.next = head
                break
            i += 1

        rev_end.next = end.next
        start_end.next = rev

        return start.next


def from_list(data: ListNode):
    response = []
    cur = data
    while cur != None:
        response.append(cur.val)
        cur = cur.next
    return response


def gen_list(data: list):
    last = None
    for x in reversed(data):
        cur = ListNode(x, last)
        last = cur
    return last


def do_test(i: int, s, a, b, r):
    c = Solution()
    resp = c.reverseBetween(gen_list(s), a, b)
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5])
    do_test(1, [5], 1, 1, [5])
    do_test(2, [1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1])
    do_test(3, [1, 2, 3, 4, 5], 1, 4, [4, 3, 2, 1, 5])

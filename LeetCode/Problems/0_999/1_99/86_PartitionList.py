from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l, r = ListNode(0), ListNode(0)
        lh, rh = l, r
        while head:
            if head.val >= x:
                r.next = head
                r = r.next
            else:
                l.next = head
                l = l.next
            cur = head
            head = head.next
            cur.next = None
        l.next = rh.next
        return lh.next

    def partition_1(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low = ListNode(-1)
        lastLow = low
        high = ListNode(-1)
        lastHeigh = high

        while head:
            if head.val >= x:
                lastHeigh.next = head
                lastHeigh = lastHeigh.next
            else:
                lastLow.next = head
                lastLow = lastLow.next
            head = head.next
            lastLow.next = None
            lastHeigh.next = None

        lastLow.next = high.next
        return low.next


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


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.partition(gen_list(s), n)
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5])
    do_test(1, [2, 1], 2, [1, 2])

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next

        return None

    def detectCycle_i(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """internet solution"""
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


def from_list(data: ListNode):
    response = []
    cur = data
    while cur != None:
        response.append(cur.val)
        cur = cur.next
    return response


def gen_list(data: list, r: int):
    m = dict()
    last = None
    first = None
    for x in reversed(data):
        cur = ListNode(x, last)
        if not first:
            first = cur
        m[len(m)] = cur
        last = cur
    if r >= 0:
        first.next = m[len(m) - r - 1]
    return last


def do_test(i: int, s, r):
    c = Solution()
    l = gen_list(s, r)
    resp = c.detectCycle(l)
    cycle = l
    if r >= 0:
        for _ in range(r):
            cycle = cycle.next
    else:
        cycle = None

    if resp == cycle:
        print("OK", i)
    else:
        print("NOK", i, "expected", cycle, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 2, 0, -4], 1)
    do_test(1, [1, 2], 0)
    do_test(2, [1], -1)

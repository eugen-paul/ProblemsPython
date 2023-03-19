from typing import Deque, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        s1 = Deque()
        s2 = set()

        while head:
            if len(s1) != 0 and s1[-1] == head.val:
                s2.add(head.val)
            else:
                s1.append(head.val)
            head = head.next

        resp = ListNode(-200)
        resp_head = resp

        while s1:
            node = s1.popleft()
            if node not in s2:
                resp.next = ListNode(node)
                resp = resp.next

        return resp_head.next

    def deleteDuplicates_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        resp = ListNode(-200)
        resp_head = resp

        node_to_check = head
        val_to_check = node_to_check.val

        cur = head.next

        while cur:
            v = cur.val
            if v == val_to_check:
                node_to_check = None
            elif node_to_check is not None:
                node_to_check.next = None
                resp.next = node_to_check
                resp = node_to_check
                node_to_check = cur
            else:
                node_to_check = cur
            val_to_check = v
            cur = cur.next

        if node_to_check:
            resp.next = node_to_check

        return resp_head.next


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


def do_test(i: int, s, r):
    c = Solution()
    resp = c.deleteDuplicates(gen_list(s))
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 3, 4, 4, 5], [1, 2, 5])
    do_test(1, [1, 1, 1, 2, 3], [2, 3])
    do_test(2, [], [])
    do_test(3, [1, 1, 1, 2, 3, 4, 7, 7, 7], [2, 3, 4])
    do_test(4, [1, 1, 1, 7, 7, 7], [])
    do_test(5, [1, 1, 1, 4, 7, 7, 7], [4])
    do_test(6, [1], [1])
    do_test(7, [1, 1], [])

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first_pos = head
        second_pos = head
        diff = 0

        while first_pos:
            if diff > n:
                second_pos = second_pos.next
            else:
                diff += 1
            first_pos = first_pos.next

        if diff == n:
            head = head.next
        else:
            second_pos.next = second_pos.next.next

        return head

    def removeNthFromEnd_fast(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first_pos = head

        for _ in range(n):
            first_pos = first_pos.next

        if not first_pos:
            return head.next

        second_pos = head

        while first_pos.next:
            second_pos = second_pos.next
            first_pos = first_pos.next

        second_pos.next = second_pos.next.next

        return head

    def removeNthFromEnd_alt(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_buffer = []

        current = head
        while current is not None:
            list_buffer.append(current)
            current = current.next

        if n == 1:
            if len(list_buffer) > 1:
                list_buffer[len(list_buffer) - 2].next = None
                return head
            elif len(list_buffer) == 1:
                return None

        delete_pos = len(list_buffer) - n
        if delete_pos == 0:
            return head.next

        list_buffer[delete_pos-1].next = list_buffer[delete_pos].next

        return head

    def removeNthFromEnd_slow(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        current = head
        while current is not None:
            current = current.next
            list_len += 1

        if list_len == 1 and n == 1:
            return None

        toDelete = list_len - n - 1
        if toDelete == -1:
            return head.next

        pos = 0
        current = head
        while pos < toDelete:
            current = current.next
            pos += 1

        current.next = current.next.next

        return head


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
    resp = c.removeNthFromEnd(gen_list(s), n)
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
    do_test(1, [1], 1, [])
    do_test(2, [1, 2], 1, [1])
    do_test(3, [1, 2], 2, [2])

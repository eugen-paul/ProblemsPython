from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None or head.next is None:
            return head

        list_len = 1
        current_pointer = head
        while current_pointer.next:
            list_len += 1
            current_pointer = current_pointer.next

        k = k % list_len
        if k == 0:
            return head

        current_pointer.next = head

        current_pointer = head
        for _ in range(list_len - k - 1):
            current_pointer = current_pointer.next

        tmp = current_pointer
        current_pointer = current_pointer.next
        tmp.next = None
        resp = current_pointer

        return resp

    def rotateRight_2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None or head.next is None:
            return head

        list_len = 0
        current_pointer = head
        while current_pointer:
            list_len += 1
            current_pointer = current_pointer.next

        k = k % list_len
        if k == 0:
            return head

        current_pointer = head
        for _ in range(list_len - k - 1):
            current_pointer = current_pointer.next

        tmp = current_pointer
        current_pointer = current_pointer.next
        tmp.next = None
        resp = current_pointer
        for _ in range(k-1):
            current_pointer = current_pointer.next
        current_pointer.next = head

        return resp


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
    resp = c.rotateRight(gen_list(s), n)
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])
    do_test(1, [0, 1, 2], 4, [2, 0, 1])
    do_test(2, [], 4, [])
    do_test(3, [1, 2], 0, [1, 2])
    do_test(4, [1], 9, [1])

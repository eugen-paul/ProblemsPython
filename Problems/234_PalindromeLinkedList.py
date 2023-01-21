from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        to_count = head
        while to_count:
            to_count = to_count.next
            length += 1

        if length == 1:
            return True

        pointer = head
        first = ListNode(-1, None)
        for _ in range(length // 2):
            nxt = pointer.next
            pointer.next = first.next
            first.next = pointer
            pointer = nxt

        if length % 2 == 1:
            pointer = pointer.next

        first = first.next
        for _ in range(length // 2):
            if first.val != pointer.val:
                return False
            first = first.next
            pointer = pointer.next

        return True

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        length = 0
        to_count = head
        while to_count:
            to_count = to_count.next
            length += 1

        if length == 1:
            return True

        middle: Optional[ListNode] = head
        for _ in range(length // 2):
            middle = middle.next

        if length % 2 == 1:
            middle = middle.next

        last = ListNode(-1, None)
        for _ in range(length // 2):
            nxt = middle.next
            middle.next = last.next
            last.next = middle
            middle = nxt

        last = last.next
        for _ in range(length // 2):
            if last.val != head.val:
                return False
            last = last.next
            head = head.next

        return True

    def isPalindrome_fast(self, head: Optional[ListNode]) -> bool:
        r = []
        while head:
            r.append(head.val)
            head = head.next
        return r == r[::-1]


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
    resp = c.isPalindrome(gen_list(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 2, 2, 1], True)
    do_test(1, [1, 2], False)
    do_test(2, [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0], True)
    do_test(3, [0, 1, 0], True)
    do_test(4, [0], True)
    do_test(5, [0, 1, 2], False)

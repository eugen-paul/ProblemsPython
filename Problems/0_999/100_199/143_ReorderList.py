from typing import Deque, List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        buff = Deque()
        cur = head
        while cur:
            buff.append(cur)
            cur = cur.next

        buff.popleft()
        cur = head
        while buff:
            cur.next = buff.pop()
            cur = cur.next
            if buff:
                cur.next = buff.popleft()
                cur = cur.next
            cur.next = None

    def reorderList_1(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # mid
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second
        curr, prev = slow.next, None
        slow.next = None  # set the next of the slow to None to break the link
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev

        # merge
        first_half = head
        while first_half and second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2


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
    l = gen_list(s)
    c.reorderList(l)
    if from_list(l) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(l))


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4], [1, 4, 2, 3])
    do_test(1, [1, 2, 3, 4, 5], [1, 5, 2, 4, 3])

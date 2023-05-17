from typing import Deque, List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l += 1

        q = Deque()
        l /= 2
        cur = head
        while l:
            q.append(cur.val)
            l -= 1
            cur = cur.next

        resp = 0
        while cur:
            resp = max(resp, cur.val + q.pop())
            cur = cur.next

        return resp

    def pairSum_1(self, head: Optional[ListNode]) -> int:
        q = Deque()
        while head:
            q.append(head.val)
            head = head.next
        resp = 0
        while q:
            resp = max(resp, q.pop() + q.popleft())
        return resp

    def pairSum_i(self, head):
        """sample solution"""
        slow, fast = head, head
        maximumSum = 0

        # Get middle of the linked list.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half of the linked list.
        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        start = head
        while prev:
            maximumSum = max(maximumSum, start.val + prev.val)
            prev = prev.next
            start = start.next

        return maximumSum


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
    resp = c.pairSum(gen_list(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [5, 4, 2, 1], 6)
    do_test(1, [4, 2, 2, 3], 7)
    do_test(2, [1, 100000], 100001)

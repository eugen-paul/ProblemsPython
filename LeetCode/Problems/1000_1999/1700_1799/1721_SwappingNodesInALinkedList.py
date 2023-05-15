from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1

        cur = head
        pos = 0
        while cur:
            if pos == k-1:
                a = cur
            if pos == l - k:
                b = cur
            cur = cur.next
            pos += 1
        a.val, b.val = b.val, a.val
        return head

    def swapNodes_i(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """internet solution:
        https://leetcode.com/problems/swapping-nodes-in-a-linked-list/solutions/3526154/python-java-elegant-short-fast-slow-pointers-one-pass/
        """
        first = second = head
        for _ in range(k - 1):
            first = first.next

        tail = first
        while tail.next:
            second = second.next
            tail = tail.next

        first.val, second.val = second.val, first.val
        return head

    def swapNodes_2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1

        if k * 2 - 1 == l or l == 1:
            return head

        if k > l - k + 1:
            k = l - k + 1

        pre_a, pre_b = None, None
        resp = ListNode(0)
        resp.next = head

        cur = resp
        pos = 0
        while cur:
            if pos == k-1:
                pre_a = cur
            if pos == l - k:
                pre_b = cur
            cur = cur.next
            pos += 1

        a, b = pre_a.next, pre_b.next
        post_a = pre_a.next.next
        post_b = pre_b.next.next

        if a.next == b:
            pre_a.next = b
            b.next = a
            a.next = post_b
        else:
            pre_a.next = b
            pre_a.next.next = post_a
            pre_b.next = a
            pre_b.next.next = post_b

        return resp.next

    def swapNodes_1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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
        a = from_list(head)
        k = k-1
        a[k], a[-k-1] = a[-k-1], a[k]
        return gen_list(a)


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


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.swapNodes(gen_list(s), n)
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5])
    do_test(1, [7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5, [7, 9, 6, 6, 8, 7, 3, 0, 9, 5])
    do_test(2, [1, 2, 3, 4, 5], 3, [1, 2, 3, 4, 5])
    do_test(3, [1], 1, [1])
    do_test(4, [1, 2], 1, [2, 1])
    do_test(5, [1, 2], 2, [2, 1])
    do_test(6, [1, 2, 3], 1, [3, 2, 1])

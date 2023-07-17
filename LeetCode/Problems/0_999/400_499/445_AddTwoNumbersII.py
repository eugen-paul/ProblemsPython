from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = 0, 0
        while l1:
            a = a*10 + l1.val
            l1 = l1.next
        while l2:
            b = b*10 + l2.val
            l2 = l2.next
        c = a+b
        if c == 0:
            return ListNode(0)

        last = None
        while c:
            cur = ListNode(c % 10, next=last)
            c //= 10
            last = cur
        return last

    def addTwoNumbers_1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = int("".join([str(i) for i in from_list(l1)]))
        b = int("".join([str(i) for i in from_list(l2)]))

        c = a+b

        return gen_list([int(i) for i in str(c)])


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
    resp = c.addTwoNumbers(gen_list(s), gen_list(n))
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7])
    do_test(1, [2, 4, 3], [5, 6, 4], [8, 0, 7])
    do_test(2, [0], [0], [0])

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pos = ListNode()
        result = pos

        p1 = l1
        p2 = l2
        rest = 0

        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

            to_add = v1 + v2 + rest
            rest = to_add // 10
            to_add = to_add % 10

            pos.next = ListNode(to_add)
            pos = pos.next

        if rest != 0:
            pos.next = ListNode(rest)

        return result.next


def gen_list(data: list):
    last = None
    for x in reversed(data):
        cur = ListNode(x, last)
        last = cur
    return last


def from_list(data: ListNode):
    response = []
    cur = data
    while cur != None:
        response.append(cur.val)
        cur = cur.next
    return response


if __name__ == "__main__":
    s = Solution()
    p1 = gen_list([2, 4, 3])
    p2 = gen_list([5, 6, 4])
    t = from_list(s.addTwoNumbers(p1, p2))
    if t == [7, 0, 8]:
        print("OK 1")

    p1 = gen_list([0])
    p2 = gen_list([0])
    t = from_list(s.addTwoNumbers(p1, p2))
    if t == [0]:
        print("OK 2")

    p1 = gen_list([9, 9, 9, 9, 9, 9, 9])
    p2 = gen_list([9, 9, 9, 9])
    t = from_list(s.addTwoNumbers(p1, p2))
    if t == [8, 9, 9, 9, 0, 0, 0, 1]:
        print("OK 3")

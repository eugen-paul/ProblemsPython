from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = 0
        tmp = headA
        while tmp:
            l1 += 1
            tmp = tmp.next

        l2 = 0
        tmp = headB
        while tmp:
            l2 += 1
            tmp = tmp.next

        if l1 > l2:
            headA, headB = headB, headA
            l1, l2 = l2, l1

        for _ in range(l2-l1):
            headB = headB.next

        while headA != headB and headA and headB:
            headA = headA.next
            headB = headB.next

        return headA

    def getIntersectionNode_1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next

        while headB:
            if headB in s:
                return headB
            headB = headB.next

        return None

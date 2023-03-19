from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        resp = head
        while list1 and list2:
            if list1.val > list2.val:
                resp.next = list2
                list2 = list2.next
            else:
                resp.next = list1
                list1 = list1.next
            resp = resp.next

        if list1:
            resp.next = list1
        else:
            resp.next = list2

        return head.next

    def mergeTwoLists_1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        resp = head
        while list1 and list2:
            if list1.val > list2.val:
                resp.next = list2
                list2 = list2.next
            else:
                resp.next = list1
                list1 = list1.next
            resp = resp.next

        while list1:
            resp.next = list1
            list1 = list1.next
            resp = resp.next

        while list2:
            resp.next = list2
            list2 = list2.next
            resp = resp.next

        return head.next


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
    resp = c.mergeTwoLists(gen_list(s), gen_list(n))
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
    do_test(1, [], [], [])
    do_test(2, [1], [], [1])
    do_test(3, [], [1], [1])

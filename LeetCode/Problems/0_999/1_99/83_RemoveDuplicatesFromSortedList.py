from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        last_p = head
        last_v = head.val

        current = head.next
        while current:
            if last_v == current.val:
                last_p.next = current.next
            else:
                last_p = current
                last_v = current.val
            current = current.next

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


def do_test(i: int, s, r):
    c = Solution()
    resp = c.deleteDuplicates(gen_list(s))
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 1, 2], [1, 2])
    do_test(1, [1, 1, 2, 3, 3], [1, 2, 3])
    do_test(2, [], [])

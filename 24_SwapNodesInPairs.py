from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        last = None
        while current:
            if last is not None:
                current.val, last.val = last.val, current.val
                last = None
            else:
                last = current
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
    resp = c.swapPairs(gen_list(s))
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4], [2, 1, 4, 3])
    do_test(1, [], [])
    do_test(2, [1], [1])
    do_test(3, [1, 2, 3], [2, 1, 3])

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def from_list(data: ListNode) -> List[int]:
    response = []
    cur = data
    while cur != None:
        response.append(cur.val)
        cur = cur.next
    return response


def gen_list(data: list, r: int):
    m = dict()
    last = None
    first = None
    for x in reversed(data):
        cur = ListNode(x, last)
        if not first:
            first = cur
        m[len(m)] = cur
        last = cur
    if r >= 0:
        first.next = m[len(m) - r - 1]
    return last


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.hasCycle(gen_list(s, n))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [3, 2, 0, -4], 1, True)
    do_test(1, [1, 2], 0, True)
    do_test(2, [1], -1, False)

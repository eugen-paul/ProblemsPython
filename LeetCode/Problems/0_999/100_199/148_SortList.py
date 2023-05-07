from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def get_mid(node: Optional[ListNode]) -> Optional[ListNode]:
            slow, fast = node, node.next
            while slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            resp = ListNode(0)

            curr = resp
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
                curr.next = None

            if l1:
                curr.next = l1
            else:
                curr.next = l2

            return resp.next

        def sort_list(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node or not node.next:
                return node

            mid = get_mid(node)
            tmp = mid.next
            mid.next = None

            left = sort_list(node)
            right = sort_list(tmp)
            return merge_lists(left, right)

        return sort_list(head)

    def sortList_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tuples: List[Tuple[int, ListNode]] = []

        def init_tuples(data: ListNode):
            cur = data
            while cur != None:
                tuples.append((cur.val, cur))
                cur = cur.next

        init_tuples(head)
        tuples.sort(key=lambda a: a[0])

        resp = ListNode(0)
        last = resp
        for t in tuples:
            last.next = t[1]
            last = t[1]
            last.next = None

        return resp.next

    def sortList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
        data = from_list(head)

        data.sort()

        return gen_list(data)


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
    resp = c.sortList(gen_list(s))
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [4, 2, 1, 3], [1, 2, 3, 4])
    do_test(1, [-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])
    do_test(2, [], [])
    do_test(3, [1], [1])
    do_test(4, [4, 19, 14, 5, -3, 1, 8, 5, 11, 15], [-3, 1, 4, 5, 5, 8, 11, 14, 15, 19])

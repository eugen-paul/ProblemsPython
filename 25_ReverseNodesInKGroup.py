from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        # Pseudo-node, since you need an element (end_of_last_array) for the each pass of the while loop.
        respone_dummy = ListNode(0, head)
        end_of_last_array = respone_dummy

        global_current = head

        # Counter for the passing nodes.
        counter = 1
        while global_current:
            # If k nodes have been passed through, invert the last sublist.
            if counter == k:
                # Create a pseudo list and add each node to the top of the list.
                reverse_begin = end_of_last_array.next
                reverse_end = end_of_last_array.next
                for _ in range(k-1):
                    nxt = reverse_end.next
                    reverse_end.next = nxt.next
                    nxt.next = reverse_begin
                    reverse_begin = nxt
                # Adjust all necessary pointers.
                end_of_last_array.next = reverse_begin
                end_of_last_array = reverse_end
                global_current = reverse_end.next
                counter = 1
            else:
                counter += 1
                global_current = global_current.next

        return respone_dummy.next

    def reverseKGroup_3(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        respone_dummy = ListNode(0, head)
        sub_begin = head
        global_current = head
        end_of_last_array = respone_dummy

        counter = 1
        while global_current:
            if counter == k:
                sub_first = sub_begin
                sub_last = sub_begin
                sub_current = sub_begin.next
                for _ in range(k-1):
                    sub_last.next = sub_current.next
                    sub_current.next = sub_first
                    sub_first = sub_current
                    sub_current = sub_last.next
                counter = 1
                sub_begin = sub_current
                end_of_last_array.next = sub_first
                end_of_last_array = sub_last
                global_current = sub_current
            else:
                counter += 1
                global_current = global_current.next

        return respone_dummy.next

    def reverseKGroup_2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        data = list()

        first = head
        current = head
        while current:
            data.append(current.val)
            current = current.next
            if len(data) == k:
                for _ in range(k):
                    first.val = data.pop()
                    first = first.next

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


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.reverseKGroup(gen_list(s), n)
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])
    do_test(1, [1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])
    do_test(2, [1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1])
    do_test(3, [1], 1, [1])
    do_test(4, [1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5])
    do_test(5, [1, 2, 3, 4, 5, 6], 2, [2, 1, 4, 3, 6, 5])

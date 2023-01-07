from typing import List, Dict, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list_copy: List[Optional[ListNode]] = list()
        for x in lists:
            if x is not None:
                list_copy.append(x)

        response = ListNode()
        head = response
        while len(list_copy) > 1:
            min_value = 100_000
            min_index = -1
            for i, v in enumerate(list_copy):
                if v.val < min_value:
                    min_index = i
                    min_value = v.val
            response.next = list_copy[min_index]
            response = response.next
            if list_copy[min_index].next is None:
                list_copy.pop(min_index)
            else:
                list_copy[min_index] = list_copy[min_index].next

        for rest in list_copy:
            response.next = rest

        return head.next

    def mergeKLists_1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m: Dict[int, ListNode] = dict()
        for i, l in enumerate(lists):
            if l is not None:
                m[i] = l

        response = ListNode()
        head = response
        while len(m) > 1:
            min_value = 100_000
            min_index = -1
            for k, v in m.items():
                if v.val < min_value:
                    min_index = k
                    min_value = v.val
            response.next = m[min_index]
            response = response.next
            if m[min_index].next is None:
                m.pop(min_index)
            else:
                m[min_index] = m[min_index].next

        for rest in m:
            response.next = m[rest]

        return head.next


def from_list(data: ListNode):
    response = []
    current = data
    while current != None:
        response.append(current.val)
        current = current.next
    return response


def gen_list(data: list):
    last = None
    for x in reversed(data):
        cur = ListNode(x, last)
        last = cur
    return last


def do_test(i: int, s, r):
    c = Solution()
    data = []
    for l in s:
        data.append(gen_list(l))
    resp = c.mergeKLists(data)
    if from_list(resp) == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", from_list(resp))


if __name__ == "__main__":
    do_test(0, [[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])
    do_test(1, [], [])
    do_test(2, [[1]], [1])
    do_test(3, [[1, 2], [5, 6]], [1, 2, 5, 6])
    do_test(4, [[5, 6], [1, 2]], [1, 2, 5, 6])
    do_test(5, [[], [], []], [])
    do_test(6, [[], [1], []], [1])

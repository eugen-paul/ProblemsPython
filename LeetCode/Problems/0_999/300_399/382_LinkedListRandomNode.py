import random
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Dumb solution"""
    def __init__(self, head: Optional[ListNode]):
        self.data = head
        self.pos = head

    def getRandom(self) -> int:
        for _ in range(random.randint(0, 50)):
            self.pos = self.pos.next
            if not self.pos:
                self.pos = self.data
        return self.pos.val


class Solution_1:

    def __init__(self, head: Optional[ListNode]):
        def from_list(data: ListNode) -> List[int]:
            response = []
            cur = data
            while cur != None:
                response.append(cur.val)
                cur = cur.next
            return response
        self.data = from_list(head)

    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

def from_list(data: ListNode) -> List[int]:
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
    c = Solution(gen_list(n[0]))
    resp = [None]
    for i in range(1, len(n)):
        resp.append(c.getRandom())
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0,
            ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"],
            [[[1, 2, 3]], [], [], [], [], []],
            [None, 1, 3, 2, 2, 3]
            )

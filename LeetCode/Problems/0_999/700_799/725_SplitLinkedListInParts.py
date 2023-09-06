from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next

        resp = []
        cur = head

        while k > 0:
            if cnt % k == 0:
                tmpCnt = cnt // k
            else:
                tmpCnt = cnt // k + 1
            resp.append(cur)
            for _ in range(tmpCnt-1):
                cur = cur.next
            if cur:
                tmp = cur.next
                cur.next = None
                cur = tmp
            cnt -= tmpCnt
            k -= 1

        return resp

    def splitListToParts(self, root, k):
        """sample solution"""
        cur = root
        for N in range(1001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur:
                    cur = cur.next
            ans.append(head.next)
        return ans


def from_list(data: ListNode) -> List[int]:
    if data is None:
        return []
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


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.splitListToParts(gen_list(s), n)
    if len(resp) != n:
        print("NOK", i, "expectedLen", n, "responseLen", len(resp))
        return

    while resp:
        tmp = resp.pop(0)
        tmpr = r.pop(0)
        if from_list(tmp) != tmpr:
            print("NOK", i, "expected", tmpr, "response", from_list(tmp))
            return
    print("OK", i)


if __name__ == "__main__":
    do_test(0, [1, 2, 3], 5, [[1], [2], [3], [], []])
    do_test(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]])

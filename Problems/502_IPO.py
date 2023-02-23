import heapq
from typing import List, Dict, Tuple, Counter

from math import inf
from typing import List


class SegmentTree:
    tree: List[int]
    source_array_len: int
    std_res = (0, 0, 0)

    def __init__(self, arr: List[int]):
        self.source_array_len = len(arr)
        self.tree = [0] * (2 * self.source_array_len)

        for i in range(self.source_array_len):
            self.tree[self.source_array_len + i] = arr[i]

        for i in range(self.source_array_len - 1, 0, -1):
            self.tree[i] = self._op(self.tree[i << 1], self.tree[i << 1 | 1])

    def _op(self, a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Tuple[int, int, int]:
        if a[1] > b[1]:
            return a
        else:
            return b

    def updateTreeNode(self, p: int, value: int):
        self.tree[p + self.source_array_len] = value
        p = p + self.source_array_len
        i = p
        while i > 1:
            self.tree[i >> 1] = self._op(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l: int, r: int) -> Tuple[int, int, int]:
        res: Tuple[int, int, int] = self.std_res

        l += self.source_array_len
        r += self.source_array_len + 1

        while l < r:
            if (l & 1):
                res = self._op(res, self.tree[l])
                l += 1

            if (r & 1):
                r -= 1
                res = self._op(res, self.tree[r])
            l >>= 1
            r >>= 1

        return res


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        s = [(a, b) for a, b in zip(capital, profits)]
        s.sort()
        p = list()
        i = 0

        while True:
            while i < len(s) and w >= s[i][0]:
                heapq.heappush(p, -s[i][1])
                i += 1
            if i > 0 and len(p) > 0:
                w += (heapq.heappop(p) * -1)
                k -= 1
                if k == 0:
                    break
            else:
                break

        return w

    def findMaximizedCapital_1(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        s = [(a, b) for a, b in zip(capital, profits)]
        s.sort()
        s = [(a[0], a[1], i) for i, a in enumerate(s)]

        tree: SegmentTree = SegmentTree(s)

        def pos_of_best(cur_capital: int) -> int:
            l, r = 0, len(s)-1
            while l <= r:
                m = (r+l) // 2
                if (s[m][0] > cur_capital):
                    r = m-1
                elif (s[m][0] <= cur_capital):
                    l = m+1
            return l-1

        for _ in range(k):
            pos = pos_of_best(w)
            if pos == -1:
                break
            el = s[pos]
            sub_w = tree.query(0, el[2])
            w += sub_w[1]
            tree.updateTreeNode(sub_w[2], (0, 0, 0))

        return w


def do_test(i: int, s, w, pr, ca, r):
    c = Solution()
    resp = c.findMaximizedCapital(s, w, pr, ca)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, 0, [1, 2, 3], [0, 1, 1], 4)
    do_test(1, 3, 0, [1, 2, 3], [0, 1, 2], 6)
    do_test(2, 3, 0, [1, 2, 3], [0, 10, 2], 1)
    do_test(3, 2, 0, [10, 2, 3], [0, 10, 2], 13)

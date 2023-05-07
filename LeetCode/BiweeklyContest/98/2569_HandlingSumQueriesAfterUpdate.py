from typing import List, Dict, Tuple, Counter
from math import inf
from typing import List


class LazySegmentTree:
    tree: List[int]
    source_array_len: int
    lazy: List[int]
    std_res: int = 0

    def __init__(self, arr: List[int]):
        self.source_array_len = len(arr)
        self.tree = [0] * (len(arr) * 4)
        self.lazy = [0] * (len(arr) * 4)
        self._build(arr, 0, self.source_array_len - 1, 0)

    def _build(self, arr: List[int], ss: int, se: int, si: int):
        if (ss > se):
            return

        if (ss == se):
            self.tree[si] = arr[ss]
            return

        mid = (ss + se) // 2
        self._build(arr, ss, mid, si * 2 + 1)
        self._build(arr, mid + 1, se, si * 2 + 2)
        self.tree[si] = self._op(self.tree[si * 2 + 1], self.tree[si * 2 + 2])

    def _op(self, a: int, b: int) -> int:
        """operation to get response. override the op if you wand to get, max/min/sum/...\n
            !!! Don'n forgen to edit self.std_res !!!
        """
        return a+b

    def _compute_tree_from_lazy(self, si: int, ss: int, se: int):
        self.tree[si] += (se - ss + 1) * self.lazy[si]

    def _compute_lazy_from_lazy(self, si: int, sc: int):
        self.lazy[sc] += self.lazy[si]

    def _compute_tree_from_diff(self, si: int, ss: int, se: int, diff: int):
        self.tree[si] += (se - ss + 1) * diff

    def _compute_lazy_from_diff(self, sc: int, diff: int):
        self.lazy[sc] += diff

    def _update_range_util(self, si: int, ss: int, se: int, us: int, ue: int, diff: int):
        if (self.lazy[si] != 0):
            self._compute_tree_from_lazy(si, ss, se)
            if (ss != se):
                self._compute_lazy_from_lazy(si, si * 2 + 1)
                self._compute_lazy_from_lazy(si, si * 2 + 2)
            self.lazy[si] = 0

        if (ss > se or ss > ue or se < us):
            return

        if (ss >= us and se <= ue):
            self._compute_tree_from_diff(si, ss, se, diff)
            if (ss != se):
                self._compute_lazy_from_diff(si * 2 + 1, diff)
                self._compute_lazy_from_diff(si * 2 + 2, diff)
            return

        mid = (ss + se) // 2
        self._update_range_util(si * 2 + 1, ss, mid, us, ue, diff)
        self._update_range_util(si * 2 + 2, mid + 1, se, us, ue, diff)
        self.tree[si] = self._op(self.tree[si * 2 + 1], self.tree[si * 2 + 2])

    def update_range(self, us: int, ue: int, diff: int):
        self._update_range_util(0, 0, self.source_array_len - 1, us, ue, diff)

    def _get_sum_util(self, ss: int, se: int, qs: int, qe: int, si: int) -> int:
        if (self.lazy[si] != 0):
            self._compute_tree_from_lazy(si, ss, se)
            if (ss != se):
                self._compute_lazy_from_lazy(si, si * 2 + 1)
                self._compute_lazy_from_lazy(si, si * 2 + 2)
            self.lazy[si] = 0

        if (ss > se or ss > qe or se < qs):
            return self.std_res

        if (ss >= qs and se <= qe):
            return self.tree[si]

        mid = (ss + se) // 2
        res_left = self._get_sum_util(ss, mid, qs, qe, 2 * si + 1)
        res_right = self._get_sum_util(mid + 1, se, qs, qe, 2 * si + 2)
        return self._op(res_left, res_right)

    def get_sum(self, qs: int, qe: int) -> int:
        if (qs < 0 or qs > qe):
            print("Invalid Input")
            return -1

        return self._get_sum_util(0, self.source_array_len - 1, qs, qe, 0)


class LazySegmentTreeSwap (LazySegmentTree):
    std_res = -inf

    def _op(self, a, b) -> int:
        return a+b

    def _compute_tree_from_lazy(self, si: int, ss: int, se: int):
        self.tree[si] = (se - ss + 1) - self.tree[si]

    def _compute_lazy_from_lazy(self, si: int, sc: int):
        self.lazy[sc] = (self.lazy[si] + self.lazy[sc]) % 2

    def _compute_tree_from_diff(self, si: int, ss: int, se: int, diff: int):
        self.tree[si] = (se - ss + 1) - self.tree[si]

    def _compute_lazy_from_diff(self, sc: int, diff: int):
        self.lazy[sc] = (diff + self.lazy[sc]) % 2


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        tree = LazySegmentTreeSwap(nums1)
        sum_2 = sum(nums2)

        resp = list()
        for q in queries:
            if q[0] == 1:
                tree.update_range(q[1], q[2], 1)
            elif q[0] == 2:
                sum_2 += tree.get_sum(0, len(nums1)-1) * q[1]
            else:
                resp.append(sum_2)

        return resp

    def handleQuery_inet(self, A, B, queries):
        """internet_solution"""
        x = sum(a << i for i, a in enumerate(A))
        cur = sum(B)
        res = []
        for i, j, k in queries:
            if i == 1:
                x ^= (1 << j) - 1
                x ^= (1 << k+1) - 1
            elif i == 2:
                cur += j * x.bit_count()
            else:
                res.append(cur)
        return res

    def handleQuery_2(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """better but still too slow"""
        count_1 = sum(nums1)
        sum_2 = sum(nums2)

        resp = list()
        for q in queries:
            if q[0] == 1:
                for i in range(q[1], q[2]+1):
                    if nums1[i] == 0:
                        nums1[i] = 1
                        count_1 += 1
                    else:
                        nums1[i] = 0
                        count_1 -= 1
            elif q[0] == 2:
                sum_2 += count_1 * q[1]
            else:
                resp.append(sum_2)

        return resp

    def handleQuery_1(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """too slow"""
        resp = list()
        for q in queries:
            if q[0] == 1:
                for i in range(q[1], q[2]+1):
                    if nums1[i] == 0:
                        nums1[i] = 1
                    else:
                        nums1[i] = 0
            elif q[0] == 2:
                nums2 = [a*q[1] + b for a, b in zip(nums1, nums2)]
            else:
                resp.append(sum(nums2))

        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.handleQuery(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0,  [1, 0, 1], [0, 0, 0], [[1, 1, 1], [2, 1, 0], [3, 0, 0]], [3])
    do_test(1,  [1], [5], [[2, 0, 0], [3, 0, 0]], [5])
    do_test(2,
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],
            [48, 2, 32, 25, 30, 37, 32, 18, 48, 39, 34, 19, 46, 43, 30, 22, 20, 35, 28, 3, 5, 45, 39, 21, 46, 45, 12, 15],
            [[3, 0, 0], [2, 3, 0], [1, 10, 26], [2, 4, 0], [2, 18, 0]],
            [819])

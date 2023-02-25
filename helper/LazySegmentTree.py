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


class LazySegmentTreeMin (LazySegmentTree):
    std_res = inf

    def _op(self, a, b) -> int:
        return min(a, b)


class LazySegmentTreeMax (LazySegmentTree):
    std_res = -inf

    def _op(self, a, b) -> int:
        return max(a, b)


def test(tree: LazySegmentTree, f: int, t: int, r: int) -> bool:
    re = tree.get_sum(f, t)
    if re == r:
        print(f"from {f:2d} to {t:2d} = {re:2d}")
    else:
        print(f"from {f:2d} to {t:2d} = {re:2d}. ERROR. expected {r}")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    tree = LazySegmentTree(arr)

    print("initial")
    test(tree, 0, 0, 1)
    test(tree, 1, 1, 2)
    test(tree, 2, 2, 3)
    test(tree, 3, 3, 4)
    test(tree, 4, 4, 5)
    test(tree, 0, 1, 3)
    test(tree, 0, 4, 15)
    test(tree, 0, 3, 10)

    print("add 4 to [0,3]")
    tree.update_range(0, 3, 4)
    test(tree, 0, 0, 5)
    test(tree, 1, 1, 6)
    test(tree, 2, 2, 7)
    test(tree, 0, 1, 11)

    print("add 10 to [0,4]")
    tree.update_range(0, 4, 10)
    print("add 1 to  [0,2]")
    tree.update_range(0, 2, 1)
    test(tree, 0, 1, 33)
    test(tree, 2, 4, 51)
    test(tree, 0, 4, 84)

    arr = [1, 2, 3, 4, 5]
    print("test min")
    tree = LazySegmentTreeMin(arr)
    test(tree, 0, 0, 1)
    test(tree, 0, 4, 1)
    test(tree, 3, 4, 4)

    print("add 5 to [0,2]")
    tree.update_range(0, 2, 5)
    test(tree, 0, 0, 6)
    test(tree, 0, 4, 4)
    test(tree, 1, 3, 4)

    print("add 1 to [1,3]")
    tree.update_range(1, 3, 1)
    print("add 3 to [2,4]")
    tree.update_range(2, 4, 5)
    test(tree, 0, 0, 6)
    test(tree, 0, 4, 6)
    test(tree, 1, 3, 8)

from math import inf
from typing import List


class LazySegmentTree:
    """
    source: https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree-set-2/?ref=rp
    """
    tree: List[int]
    source_array_len: int
    lazy: List[int]
    std_res: int = 0

    def __init__(self, arr: List[int]):
        self.source_array_len = len(arr)
        self.tree = [0] * (len(arr) * 4)
        self.lazy = [0] * (len(arr) * 4)
        self._build(arr, 0, self.source_array_len - 1, 0)

    # A recursive function that constructs Segment Tree for array[ss..se].
    # si is index of current node in segment tree st.
    def _build(self, arr: List[int], ss: int, se: int, si: int):
        # out of range as ss can never be greater than se
        if (ss > se):
            return

        # If there is one element in array, store it in current node of segment tree and return
        if (ss == se):
            self.tree[si] = arr[ss]
            return

        # If there are more than one elements, then recur for left and right subtrees and store the sum of values in this node
        mid = (ss + se) // 2
        self._build(arr, ss, mid, si * 2 + 1)
        self._build(arr, mid + 1, se, si * 2 + 2)
        self.tree[si] = self._op(self.tree[si * 2 + 1], self.tree[si * 2 + 2])

    def _op(self, a: int, b: int) -> int:
        """operation to get response. override the op if you wand to get, max/min/sum/...\n
            !!! Don'n forgen to edit self.std_res !!!

        Args:
            a (int): value of one child
            b (int): value of other child

        Returns:
            int: response of operation
        """
        return a+b

    def _compute_tree_from_lazy(self, si: int, ss: int, se: int):
        """operation to compute tree-value from lazy value

        Args:
            si (int): index of current node in segment tree
            ss (int): Starting indexes of elements for which current nodes stores sum.
            se (int): Ending indexes of elements for which current nodes stores sum.
        """
        self.tree[si] += (se - ss + 1) * self.lazy[si]

    def _compute_lazy_from_lazy(self, si: int, sc: int):
        """operation to compute lazy-child-value from lazy-parent-value

        Args:
            si (int): index of current node in segment tree
            sc (int): index of child node in segment tree
        """
        self.lazy[sc] += self.lazy[si]

    def _compute_tree_from_diff(self, si: int, ss: int, se: int, diff: int):
        """operation to compute tree-value from lazy value

        Args:
            si (int): index of current node in segment tree
            ss (int): Starting indexes of elements for which current nodes stores sum.
            se (int): Ending indexes of elements for which current nodes stores sum.
            diff (int): diff value
        """
        self.tree[si] += (se - ss + 1) * diff

    def _compute_lazy_from_diff(self, sc: int, diff: int):
        """operation to compute lazy-child-value from lazy-parent-value

        Args:
            sc (int): index of child node in segment tree
            diff (int): diff value
        """
        self.lazy[sc] += diff

    def _update_range_util(self, si: int, ss: int, se: int, us: int, ue: int, diff: int):
        """add diff to all elements between us and ue

        Args:
            si (int): index of current node in segment tree
            ss (int): Starting indexes of elements for which current nodes stores sum.
            se (int): Ending indexes of elements for which current nodes stores sum.
            us (int): Starting indexes of update query
            ue (int): Ending indexes of update query
            diff (int): which we need to add in the range us to ue
        """

        # If lazy value is non-zero for current node of segment tree, then there are some
        # pending updates. So we need to make sure that the pending updates are done before
        # making new updates. Because this value may be used by parent after recursive calls
        # (See last line of this function)
        if (self.lazy[si] != 0):
            # Make pending updates using value stored in lazy nodes
            self._compute_tree_from_lazy(si, ss, se)

            # checking if it is not leaf node because if t is leaf node then we cannot go further
            if (ss != se):
                # We can postpone updating children we don't need their new values now.
                # Since we are not yet updating children of si,we need to set lazy flags for the children
                self._compute_lazy_from_lazy(si, si * 2 + 1)
                self._compute_lazy_from_lazy(si, si * 2 + 2)
            # Set the lazy value for current node as 0 as it has been updated
            self.lazy[si] = 0

        if (ss > se or ss > ue or se < us):
            return

        # Current segment is fully in range
        if (ss >= us and se <= ue):
            # Add the difference to current node
            self._compute_tree_from_diff(si, ss, se, diff)

            # same logic for checking leaf node or not
            if (ss != se):
                # This is where we store values in lazy nodes, rather than updating the segment tree itself
                # Since we don't need these updated values now we postpone updates by storing values in lazy[]
                self._compute_lazy_from_diff(si * 2 + 1, diff)
                self._compute_lazy_from_diff(si * 2 + 2, diff)
            return

        # If not completely in rang, but overlaps,
        # recur for children,
        mid = (ss + se) // 2
        self._update_range_util(si * 2 + 1, ss, mid, us, ue, diff)
        self._update_range_util(si * 2 + 2, mid + 1, se, us, ue, diff)

        # And use the result of children calls to update this node
        self.tree[si] = self._op(self.tree[si * 2 + 1], self.tree[si * 2 + 2])

    def update_range(self, us: int, ue: int, diff: int):
        """Function to update a range of values in segment tree

        Args:
            us (int): starting indexes of update query
            ue (int): ending indexes of update query
            diff (int): which we need to add in the range us to ue
        """
        self._update_range_util(0, 0, self.source_array_len - 1, us, ue, diff)

    def _get_sum_util(self, ss: int, se: int, qs: int, qe: int, si: int) -> int:
        """A recursive function to get the sum of values in given range of the array. The following are parameters for this function.

        Args:
            ss (int): Starting indexes of the segment represented by current node, i.e., tree[si]
            se (int): Ending indexes of the segment represented by current node, i.e., tree[si]
            qs (int): Starting indexes of query range
            qe (int): Ending indexes of query range
            si (int): Index of current node in the segment tree. Initially 0 is passed as root is always at' index 0

        Returns:
            int: sum of elements
        """

        # If lazy flag is set for current node of segment tree, then there are
        # some pending updates. So we need to make sure that the pending updates are
        # done before processing the sub sum query
        if (self.lazy[si] != 0):
            # Make pending updates to this node. Note that this node represents sum of
            # elements in arr[ss..se] and all these elements must be increased by lazy[si]
            self._compute_tree_from_lazy(si, ss, se)

            # checking if it is not leaf node because if it is leaf node then we cannot go further
            if (ss != se):
                # Since we are not yet updating children os si, we need to set lazy values for the children
                self._compute_lazy_from_lazy(si, si * 2 + 1)
                self._compute_lazy_from_lazy(si, si * 2 + 2)
            # unset the lazy value for current node as it has been updated
            self.lazy[si] = 0

        if (ss > se or ss > qe or se < qs):
            return self.std_res

        # At this point we are sure that pending lazy updates are done for
        # current node. So we can return value (same as it was for query in our previous post)

        # If this segment lies in range
        if (ss >= qs and se <= qe):
            return self.tree[si]

        # If a part of this segment overlaps with the given range
        mid = (ss + se) // 2
        res_left = self._get_sum_util(ss, mid, qs, qe, 2 * si + 1)
        res_right = self._get_sum_util(mid + 1, se, qs, qe, 2 * si + 2)
        return self._op(res_left, res_right)

    def get_sum(self, qs: int, qe: int) -> int:
        """Return sum of elements in range from qs to qe

        Args:
            qs (int): from 
            qe (int): to

        Returns:
            int: sum
        """

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

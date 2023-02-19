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
        self.tree = [0] * (len(arr) * 2)
        self.lazy = [0] * (len(arr) * 2)
        self._build(arr, 0, self.source_array_len - 1, 0)

    def _build(self, arr: List[int], ss: int, se: int, si: int):
        """ recursive function that constructs Segment Tree for array[ss..se].

        Args:
            arr (_type_): source array
            ss (int): from index of array
            se (int): to index of array
            si (int): index of current node in segment
        """
        if (ss > se):
            return

        if (ss == se):
            # leaf
            self.tree[si] = arr[ss]
            return

        mid = (ss + se) // 2
        self._build(arr, ss, mid, si * 2 + 1)
        self._build(arr, mid + 1, se, si * 2 + 2)
        # compute current node from childs values
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

    def update_range_util(self, si: int, ss: int, se: int, us: int, ue: int, diff: int):
        """update range in Tree using diff

        Args:
            si (int): index of current node in segment tree
            ss (int): Starting indexes of elements for which current nodes stores sum
            se (int): Ending indexes of elements for which current nodes stores sum
            us (int): Starting indexes of update query
            ue (int): Ending indexes of update query
            diff (int): which we need to add in the range us to ue
        """
        # If lazy value is non-zero for current node  of segment tree, then there are some
        # pending updates. So we need to make sure that  the pending updates are done before making
        # new updates. Because this value may be used by  parent after recursive calls (See last line of this
        # function)
        if (self.lazy[si] != 0):
            # Make pending updates using value stored in lazy nodes
            self.tree[si] += self.lazy[si]

            # Checking if it is not leaf node because if it is leaf node then we cannot go further
            if (ss != se):
                # We can postpone updating children we don't need their new values now.
                # Since we are not yet updating children of si, we need to set lazy flags for the children
                self.lazy[si * 2 + 1] += self.lazy[si]
                self.lazy[si * 2 + 2] += self.lazy[si]

            # Set the lazy value for current node as 0 as it has been updated
            self.lazy[si] = 0

        # Out of range
        if (ss > se or ss > ue or se < us):
            return

        # Current segment is fully in range
        if (ss >= us and se <= ue):
            # Add the difference to current node
            self.tree[si] += diff

            # Same logic for checking leaf node or not
            if (ss != se):
                # This is where we store values in lazy nodes, rather than updating the segment tree itself
                # Since we don't need these updated values now we postpone updates by storing values in lazy[]
                self.lazy[si * 2 + 1] += diff
                self.lazy[si * 2 + 2] += diff
            return

        # If not completely in range, but overlaps
        # recur for children
        mid = (ss + se) // 2
        self.update_range_util(si * 2 + 1, ss, mid, us, ue, diff)
        self.update_range_util(si * 2 + 2, mid + 1, se, us, ue, diff)

        # And use the result of children calls to update this node
        self.tree[si] = self._op(self.tree[si * 2 + 1], self.tree[si * 2 + 2])

    def update_range(self, us: int, ue: int, diff: int):
        """Function to update a range of values in segment tree

        Args:
            us (int): Starting indexes of update query
            ue (int): Ending indexes of update query
            diff (int): which we need to add in the range us to ue
        """

        self.update_range_util(0, 0, self.source_array_len - 1, us, ue, diff)

    def get_sum_util(self, ss: int, se: int, qs: int, qe: int, si: int) -> int:
        """ A recursive function to get the sum of values in a given range of the array. The following are the parameters for this function

        Args:
            ss (int): Starting indexes of the segment represented by current node
            se (int): Ending indexes of the segment represented by current node
            qs (int): Starting indexes of query range
            qe (int): Ending indexes of query range
            si (int): Index of the current node in the segment tree Initially, 0 is passed as root is always at index 0

        Returns:
            int: sum of items in range
        """

        # If lazy flag is set for current node of segment tree then there are some
        # pending updates. So we need to make sure that the pending updates are done before
        # processing the sub sum query
        if (self.lazy[si] != 0):
            # Make pending updates to this node. Note that this node represents sum of
            # elements in arr[ss..se] and all these elements must be increased by lazy[si]
            self.tree[si] += self.lazy[si]

            # Checking if it is not leaf node because if it is leaf node then we cannot go further
            if (ss != se):
                # Since we are not yet updating children os si, we need to set lazy values for the children
                self.lazy[si * 2 + 1] += self.lazy[si]
                self.lazy[si * 2 + 2] += self.lazy[si]

            # Unset the lazy value for current node as it has been updated
            self.lazy[si] = 0

        # Out of range
        if (ss > se or ss > qe or se < qs):
            return self.std_res

        # At this point, we are sure that pending lazy updates are done for current node. So we can return value

        # If this segment lies in range
        if (ss >= qs and se <= qe):
            return self.tree[si]

        # If a part of this segment overlaps with the given range
        mid = (ss + se) // 2
        return self._op(self.get_sum_util(ss, mid, qs, qe, 2 * si + 1), self.get_sum_util(mid + 1, se, qs, qe, 2 * si + 2))

    def get_sum(self, qs: int, qe: int) -> int:
        """Return sum of elements in range from index qs (query start) to qe (query end). It mainly uses getSumUtil()

        Args:
            qs (int): from index
            qe (int): to index

        Returns:
            int: response
        """

        # Check for erroneous input values
        if (qs < 0 or qe > self.source_array_len - 1 or qs > qe):
            print("Invalid Input", end="")
            return -1

        return self.get_sum_util(0, self.source_array_len - 1, qs, qe, 0)


class LazySegmentTreeMin (LazySegmentTree):
    std_res = inf

    def _op(self, a, b) -> int:
        return min(a, b)


class LazySegmentTreeMax (LazySegmentTree):
    std_res = -inf

    def _op(self, a, b) -> int:
        return max(a, b)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    tree = LazySegmentTree(arr)

    print(tree.get_sum(1, 4))
    tree.update_range(0, 3, 4)
    print(tree.get_sum(1, 4))

    tree = LazySegmentTreeMin(arr)

    print(tree.get_sum(1, 4))
    tree.update_range(0, 3, 4)
    print(tree.get_sum(1, 4))

    tree = LazySegmentTreeMax(arr)

    print(tree.get_sum(1, 4))
    tree.update_range(0, 3, 4)
    print(tree.get_sum(1, 4))

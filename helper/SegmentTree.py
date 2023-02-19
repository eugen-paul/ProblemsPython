from math import inf
from typing import List


class SegmentTree:

    # Max size of tree
    tree: List[int]
    source_array_len: int
    std_res = 0

    def __init__(self, arr: List[int]):
        """Contructor

        Args:
            arr (List[int]): array to convert to SegmentTree
        """

        self.source_array_len = len(arr)
        self.tree = [0] * (2 * self.source_array_len)

        # insert leaf nodes in tree
        for i in range(self.source_array_len):
            self.tree[self.source_array_len + i] = arr[i]

        # build the tree by calculating parents
        for i in range(self.source_array_len - 1, 0, -1):
            self.tree[i] = self._op(self.tree[i << 1], self.tree[i << 1 | 1])

    def _op(self, a: int, b: int) -> int:
        """operation to fill parent of nodes. override the op if you wand to get, max/min/sum/...\n
            !!! Don'n forgen to edit self.std_res !!!

        Args:
            a (int): value of one child
            b (int): value of other child

        Returns:
            int: response of operation
        """
        return a+b

    def updateTreeNode(self, p: int, value: int):
        """Update a tree node

        Args:
            p (int): index of node to update
            value (int): new value of the node
        """
        # set value at position p
        self.tree[p + self.source_array_len] = value
        p = p + self.source_array_len

        # move upward and update parents
        i = p

        while i > 1:
            self.tree[i >> 1] = self._op(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l: int, r: int) -> int:
        """function to get sum on interval [l, r)

        Args:
            l (int): from index inclusive
            r (int): to index inclusive

        Returns:
            int: sum
        """
        res: int = self.std_res

        # loop to find the sum in the range
        l += self.source_array_len + 1
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


class SegmentTreeMin (SegmentTree):
    std_res = inf

    def _op(self, a, b) -> int:
        return min(a, b)


# Driver Code
if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    tree: SegmentTree = SegmentTree(a)

    print(tree.query(0, 6))
    tree.updateTreeNode(2, 1)
    tree.updateTreeNode(4, 1)
    print(tree.query(0, 6))

    tree: SegmentTreeMin = SegmentTreeMin(a)
    print(tree.query(4, 10))
    tree.updateTreeNode(6, 2)
    print(tree.query(4, 10))

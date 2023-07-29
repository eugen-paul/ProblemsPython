import bisect
from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import os.path
import sys
input = sys.stdin.readline


MOD = 10**9+7
test = False


def i_int() -> int: return int(input())
def i_str() -> str: return input()[:-1]
def i_array_int() -> List[int]: return list(map(int, input().split()))
def i_array_str() -> List[str]: return i_str().split()
def i_set_int() -> Set[int]: return set(map(int, input().split()))
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


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
            if i < i ^ 1:
                self.tree[i >> 1] = self._op(self.tree[i], self.tree[i ^ 1])
            else:
                self.tree[i >> 1] = self._op(self.tree[i ^ 1], self.tree[i])
            i >>= 1

    def query(self, l: int, r: int) -> int:
        """function to get sum on interval [l, r]

        Args:
            l (int): from index inclusive
            r (int): to index inclusive

        Returns:
            int: sum
        """
        res: int = self.std_res

        # loop to find the sum in the range
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


def solve_s():
    # too slow
    for _ in range(i_int()):
        n, m = i_array_int()
        s = [int(c) for c in i_str()]
        z = 0
        for c in s:
            z <<= 1
            z += c

        v = set()

        seg = SegmentTree(s)

        for _ in range(m):
            l, r = i_array_int()

            st = 2**(l-1)-1
            st <<= n-l+1

            end = 2**(n-r)-1

            mid = seg.query(l-1, r-1)
            mid = (2**mid - 1) << (n-r)

            tmp = (st | end) & z
            tmp |= mid

            v.add(tmp)
        print(len(v))


def solve():
    for _ in range(i_int()):
        n, m = i_array_int()
        s = i_str()

        left = [i for i in range(n)]
        left[0] = -1 if s[0] == '1' else 0
        for i in range(1, len(s)):
            if s[i] != '0':
                left[i] = left[i-1]

        right = [i for i in range(n)]
        right[-1] = n if s[-1] == '0' else n-1
        for i in range(len(s)-2, -1, -1):
            if s[i] != '1':
                right[i] = right[i+1]

        s = set()
        for _ in range(m):
            l, r = i_array_int()
            a, b = right[l-1], left[r-1]
            if a > b:
                s.add((-1, -1))
            else:
                s.add((a, b))

        print(len(s))


testData = """3
6 5
101100
1 2
1 3
2 4
5 5
1 6
6 4
100111
2 2
1 4
1 3
1 2
1 1
0
1 1
""".split("\n")
# testData = list()
testDataPos = 0

if len(testData) > 1 and os.path.exists('localTestCheckFile.txt'):
    test = True

    def test_data_input():
        global testDataPos
        r = testData[testDataPos]
        testDataPos += 1
        return r + "\n"
    input = test_data_input


if __name__ == "__main__":
    solve()

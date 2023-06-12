import bisect
from collections import defaultdict
from email import header
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import os.path
import sys
import hashlib
input = sys.stdin.readline


MOD = 10**9+7
test = False


def i_int() -> int: return int(input())
def i_str() -> str: return input()[:-1]
def i_array_int() -> List[int]: return list(map(int, input().split()))
def i_array_str() -> List[str]: i_str().split()
def i_set_int() -> Set[int]: return set(map(int, input().split()))
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


class SegmentTree:

    # Max size of tree
    tree: List[bool]
    source_array_len: int
    std_res = True

    def __init__(self, arr: List[int]):
        self.source_array_len = len(arr)
        self.tree = [True] * (2 * self.source_array_len)

        # insert leaf nodes in tree
        for i in range(self.source_array_len):
            self.tree[self.source_array_len + i] = arr[i]

        # build the tree by calculating parents
        for i in range(self.source_array_len - 1, 0, -1):
            self.tree[i] = self._op(self.tree[i << 1], self.tree[i << 1 | 1])

    def _op(self, a: int, b: int) -> int:
        return a+b

    def updateTreeNode(self, p: int, value: bool):
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

    def query(self, l: int, r: int) -> bool:
        """function to get sum on interval [l, r]

        Args:
            l (int): from index inclusive
            r (int): to index inclusive

        Returns:
            int: sum
        """
        res: bool = self.std_res

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


class SegmentTreeAnd (SegmentTree):
    std_res = True

    def _op(self, a, b) -> bool:
        return a and b


def solve():
    for _ in range(i_int()):
        s1 = [c for c in i_str()]
        s2 = [c for c in i_str()]
        t, q = i_array_int()

        seg = SegmentTreeAnd([a == b for a, b in zip(s1, s2)])

        block_queue = []

        for i in range(q):

            while block_queue and block_queue[0][0] == i:
                _, pos, c1, c2 = heapq.heappop(block_queue)
                s1[pos] = c1
                s2[pos] = c2
                seg.updateTreeNode(pos, c1 == c2)

            command, *data = i_array_int()
            if command == 1:
                timeout = i+t
                pos = data[0]-1
                heapq.heappush(block_queue, (timeout, pos, s1[pos], s2[pos]))
                seg.updateTreeNode(pos, True)
            elif command == 2:
                f1, p1, f2, p2 = data
                p1 -= 1
                p2 -= 1
                if f1 == 1 and f2 == 1:
                    s1[p1], s1[p2] = s1[p2], s1[p1]
                elif f1 == 2 and f2 == 2:
                    s2[p1], s2[p2] = s2[p2], s2[p1]
                elif f1 == 1 and f2 == 2:
                    s1[p1], s2[p2] = s2[p2], s1[p1]
                elif f1 == 2 and f2 == 1:
                    s2[p1], s1[p2] = s1[p2], s2[p1]
                seg.updateTreeNode(p1, s1[p1] == s2[p1])
                seg.updateTreeNode(p2, s1[p2] == s2[p2])
            else:
                if seg.query(0, len(s1)-1):
                    print("YES")
                else:
                    print("NO")


testData = """2
codeforces
codeblocks
5 7
3
1 5
1 6
1 7
1 9
3
3
cool
club
2 5
2 1 2 2 3
2 2 2 2 4
1 2
3
3
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

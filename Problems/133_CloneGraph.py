from collections import defaultdict
from copy import deepcopy
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)

# Definition for a Node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        s: Set[int] = set()
        m: Dict[int, 'Node'] = dict()

        def rec(node: 'Node') -> 'Node':
            if not node:
                return None

            if node.val in s:
                return m[node.val]

            resp = Node(node.val)
            s.add(node.val)
            m[node.val] = resp

            for nb in node.neighbors:
                copy_nb = m.get(nb.val, rec(nb))
                resp.neighbors.append(copy_nb)
            return resp

        return rec(node)

    def cloneGraph_1(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if not node.neighbors or len(node.neighbors) == 0:
            return Node(1)

        n_list = [None] * 101
        visited: List[bool] = [False] * 101
        to_check: Deque[int] = Deque()
        n_list[1] = Node(1)
        to_check.append((1, node))

        while to_check:
            v, original_node = to_check.popleft()
            if visited[v]:
                continue
            visited[v] = True
            n = n_list[v]
            for nb in original_node.neighbors:
                if not n_list[nb.val]:
                    n_list[nb.val] = Node(nb.val)
                    to_check.append((nb.val, nb))
                n.neighbors.append(n_list[nb.val])

        return n_list[1]

    def cloneGraph_1(self, node: 'Node') -> 'Node':
        """just for fun"""
        return deepcopy(node)


def do_test(i: int, s):
    c = Solution()
    cp = c.cloneGraph(s)
    pass


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    do_test(0, n1)
    do_test(1, Node(1))
    do_test(2, None)

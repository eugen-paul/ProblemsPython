from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        """Using some help from Solution.
        Basic idea:
         - Form the complete graph with the root edges[0][0]
         - Check how many matches there are with the guesses.
         - Change the root of the tree recursively.
           - For each change, recalculate the number of matches.
             - It is enough to check whether the affected node is in guesses or not.
        """
        tree: Dict[int, Set[int]] = defaultdict(set)
        for f, t in edges:
            tree[f].add(t)
            tree[t].add(f)

        g_set: Set[Tuple[int, int]] = set()
        for f, t in guesses:
            g_set.add((f, t))

        # Form tree with the root edges[0][0]
        root = edges[0][0]
        nodes: Set[Tuple[int, int]] = set()
        visited: Set[int] = set()
        visited.add(root)

        to_check = Deque()
        to_check.append(root)

        while to_check:
            node = to_check.popleft()
            for nb in tree[node]:
                if nb in visited:
                    continue
                to_check.append(nb)
                nodes.add((node, nb))
                visited.add(nb)

        # count correct guesses for first root
        ok_count = len(g_set.intersection(nodes))
        resp = 1 if ok_count >= k else 0

        def count_and_reroot(node: int, local_ok_count: int):
            if node in visited:
                return

            for nb in tree[node]:
                if (node, nb) not in nodes:
                    if (node, nb) in g_set:
                        local_ok_count += 1
                    if (nb, node) in g_set:
                        local_ok_count -= 1

            nonlocal resp
            if local_ok_count >= k:
                resp += 1

            visited.add(node)
            for nb in tree[node]:
                count_and_reroot(nb, local_ok_count)

        visited: Set[int] = set()
        visited.add(root)
        for nb in tree[root]:
            count_and_reroot(nb, ok_count)

        return resp

    def rootCount_1(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        """Using some help from Solution.
        Basic idea:
         - Form the complete graph with the root edges[0][0]
         - Check how many matches there are with the guesses.
         - Change the root of the tree recursively.
           - For each change, recalculate the number of matches.
             - It is enough to check whether the affected node is in guesses or not.
        """
        tree: Dict[int, Set[int]] = defaultdict(set)
        for f, t in edges:
            tree[f].add(t)
            tree[t].add(f)

        g_set: Set[Tuple[int, int]] = set()
        for f, t in guesses:
            g_set.add((f, t))

        # Form tree with the root edges[0][0]
        root = edges[0][0]
        nodes: Set[Tuple[int, int]] = set()
        visited: Set[int] = set()
        visited.add(root)

        to_check = Deque()
        to_check.append(root)

        while to_check:
            node = to_check.popleft()
            for nb in tree[node]:
                if nb in visited:
                    continue
                to_check.append(nb)
                nodes.add((node, nb))
                visited.add(nb)

        # count correct guesses for first root
        ok_count = len(g_set.intersection(nodes))
        resp = 1 if ok_count >= k else 0

        def count_and_reroot(node: int, local_ok_count: int):
            if node in visited:
                return

            b = set()
            for nb in tree[node]:
                if (node, nb) not in nodes:
                    b.add((nb, node))
                    nodes.remove((nb, node))
                    nodes.add((node, nb))
                    if (node, nb) in g_set:
                        local_ok_count += 1
                    if (nb, node) in g_set:
                        local_ok_count -= 1

            nonlocal resp
            if local_ok_count >= k:
                resp += 1

            visited.add(node)
            for nb in tree[node]:
                count_and_reroot(nb, local_ok_count)

            for restore in b:
                nodes.remove((restore[1], restore[0]))
                nodes.add(restore)

        visited: Set[int] = set()
        visited.add(root)
        for nb in tree[root]:
            count_and_reroot(nb, ok_count)

        return resp

    def rootCount_i(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        """internet solution: https://leetcode.com/problems/count-number-of-possible-root-nodes/solutions/3256065/re-rooting-o-n-explained/
        java -> python
        """
        tree: Dict[int, List[int]] = defaultdict(list)
        guess_graph: Set[Tuple[int, int]] = set()
        parents: List[int] = [inf] * (len(edges)+1)
        for f, t in edges:
            tree[f].append(t)
            tree[t].append(f)
        for f, t in guesses:
            guess_graph.add((f, t))

        def fill_parent(node: int, parent: int):
            parents[node] = parent
            for child in tree[node]:
                if child == parent:
                    continue
                fill_parent(child, node)

        fill_parent(0, -1)

        correct_guesses = 0
        for i, p in enumerate(parents):
            if (p, i) in guess_graph:
                correct_guesses += 1

        resp = 1 if correct_guesses >= k else 0

        def dfs(node: int, parent: int, correct_guesses: int):
            cur: int = correct_guesses
            if (parent, node) in guess_graph:
                cur -= 1
            if (node, parent) in guess_graph:
                cur += 1
            nonlocal resp
            if cur >= k:
                resp += 1
            for child in tree[node]:
                if (child != parent):
                    dfs(child, node, cur)

        for c in tree[0]:
            dfs(c, 0, correct_guesses)

        return resp

    def rootCount_i2(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        """internet solution: https://leetcode.com/problems/count-number-of-possible-root-nodes/solutions/3256327/python-simple-dfs-with-cache-5-steps/
        """
        # Step 1 build the graph
        # contains all the edges
        # 0 -> 1,2,3 Node to list of Nodes
        GRAPH = defaultdict(list)
        # contains all the nodes
        NODES = set()

        for e in edges:
            NODES.add(e[0])
            NODES.add(e[1])
            GRAPH[e[0]].append(e[1])
            GRAPH[e[1]].append(e[0])

        # Step 2 build a set of Guesses for fast access
        # contains all the guesses
        GUESSES = set()
        for e in guesses:
            GUESSES.add((e[0], e[1]))
        # visited set
        visited = set()

        # Step 3 DFS
        # cache the result with the node and previous
        @cache
        def dfs(node: int, previous: int) -> int:
            guess_count = 0
            if (previous, node) in GUESSES:
                guess_count += 1

            # add node to visited set
            visited.add(node)

            for next_node in GRAPH[node]:
                if next_node not in visited:
                    guess_count += dfs(next_node, node)

            return guess_count

        # Step 4 Try all  the  roots
        result = 0
        for node in NODES:
            # if the root has k guesses, add 1 to the result
            if dfs(node, -1) >= k:
                result += 1
            visited = set()

        # Step 5 Return the result
        return result

    def rootCount_X(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        """total fail"""
        pass


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.rootCount(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[0, 1], [1, 2], [1, 3], [4, 2]], [[1, 3], [0, 1], [1, 0], [2, 4]], 3, 3)
    do_test(1, [[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 0], [3, 4], [2, 1], [3, 2]], 1, 5)

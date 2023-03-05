from collections import defaultdict
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

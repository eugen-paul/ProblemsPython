import math
from typing import DefaultDict, Deque, Dict, List, Set


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # convert graph to dict
        # key - node, value - set of neighbors
        m: Dict[int, Set[int]] = dict()
        for r in roads:
            if r[0] not in m:
                m[r[0]] = set()
            m[r[0]].add(r[1])
            if r[1] not in m:
                m[r[1]] = set()
            m[r[1]].add(r[0])

        # get end nodes
        rest_check = Deque()
        for k, v in m.items():
            if k != 0 and len(v) == 1:
                rest_check.append((k, 0))

        sub_nodes: Dict[int, int] = dict()
        resp = 0
        while rest_check:
            node, representatives = rest_check.pop()
            if node == 0:
                continue
            if node in sub_nodes:
                representatives += sub_nodes[node]

            all_next_nodes = m.get(node)
            if len(all_next_nodes) > 1:
                sub_nodes[node] = representatives
                continue

            representatives += 1
            next_node = all_next_nodes.pop()
            m.get(next_node).discard(node)
            rest_check.append((next_node, representatives))
            resp += math.ceil(representatives / seats)

        return resp
    
    def minimumFuelCost_internet(self, roads: List[List[int]], seats: int) -> int:
        """internet_solution"""
        graph = DefaultDict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        self.ans = 0
        
        def dfs(i, prev, people = 1):
            for x in graph[i]:
                if x == prev: continue
                people += dfs(x, i)
            self.ans += (int(math.ceil(people / seats)) if i else 0)
            return people
        
        dfs(0, 0)
        return self.ans


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minimumFuelCost(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[0, 1], [0, 2], [0, 3]], 5, 3)
    do_test(1, [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2, 7)
    do_test(2, [], 1, 0)
    do_test(3, [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 10, 6)
    do_test(4, [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 1, 10)
    do_test(5, [[1, 0], [0, 2], [3, 1], [1, 4], [5, 0]], 1, 7)
    do_test(6, [[0, 1], [2, 1], [3, 2], [4, 2], [4, 5], [6, 0], [5, 7], [8, 4], [9, 2]], 2, 16)
    do_test(7, [[0, 1], [2, 1], [3, 2], [9, 2]], 2, 6)
    do_test(8, [[0, 1], [2, 1], [3, 2], [4, 2], [9, 2]], 2, 8)
    do_test(9, [[0, 1], [2, 1], [3, 2], [4, 2], [5, 2], [9, 2]], 2, 10)
    do_test(10, [[0, 1], [0, 2], [1, 3], [1, 4]], 5, 4)

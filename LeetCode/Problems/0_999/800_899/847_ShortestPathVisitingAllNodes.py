from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def shortestPathLength_i(self, graph):
        """internet solution:
        https://leetcode.com/problems/shortest-path-visiting-all-nodes/solutions/4053514/94-74-bfs-bitmask/?envType=daily-question&envId=2023-09-17
        """
        n = len(graph)
        queue = Deque([(1 << i, i, 0) for i in range(n)])
        visited = set((1 << i, i) for i in range(n))

        while queue:
            mask, node, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))


def do_test(i: int, s, r):
    c = Solution()
    resp = c.shortestPathLength(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[1, 2, 3], [0], [0], [0]], 4)
    do_test(1, [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], 4)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

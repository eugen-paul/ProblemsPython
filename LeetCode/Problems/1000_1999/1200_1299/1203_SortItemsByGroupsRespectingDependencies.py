from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groupdict = defaultdict(list)
        for i, n in enumerate(group):
            if n == -1:
                group[i] = m
                m += 1
            groupdict[group[i]].append(i)

        graph = defaultdict(list)

        for i, prev in enumerate(beforeItems):
            for el in prev:
                if group[i] != group[el]:
                    graph[group[el]].append(group[i])

        # The function to do Topological Sort.
        def topologicalSort(vertices: int, graph: Dict[int, List[int]]) -> List[int]:

            # Create a vector to store indegrees of all vertices. Initialize all indegrees as 0.
            in_degree = [0]*vertices

            # Traverse adjacency lists to fill indegrees of vertices.  This step takes O(V + E) time
            for i in graph:
                for j in graph[i]:
                    in_degree[j] += 1

            # Create an queue and enqueue all vertices with indegree 0
            queue = []
            for i in range(vertices):
                if in_degree[i] == 0:
                    queue.append(i)

            # Initialize count of visited vertices
            cnt = 0

            # Create a vector to store result (A topological ordering of the vertices)
            top_order = []

            # One by one dequeue vertices from queue and enqueue adjacents if indegree of adjacent becomes 0
            while queue:

                # Extract front of queue (or perform dequeue) and add it to topological order
                u = queue.pop(0)
                top_order.append(u)

                # Iterate through all neighbouring nodes of dequeued node u and decrease their in-degree by 1
                for i in graph[u]:
                    in_degree[i] -= 1
                    # If in-degree becomes zero, add it to queue
                    if in_degree[i] == 0:
                        queue.append(i)

                cnt += 1

            # Check if there was a cycle
            if cnt != vertices:
                return None
            else:
                # Print topological order
                return top_order

        gr_sort = topologicalSort(m, graph)
        if gr_sort is None:
            return []

        resp = []
        for g in gr_sort:
            elements = groupdict[g]
            if len(elements) == 1:
                resp.append(elements[0])
                continue

            mp = defaultdict(int)
            for i, e in enumerate(elements):
                mp[e] = i
            graph = defaultdict(list)
            for e in elements:
                for el in beforeItems[e]:
                    if group[el] == group[e]:
                        graph[mp[el]].append(mp[e])
            el_sort = topologicalSort(len(mp), graph)
            if el_sort is None:
                return []
            for e in el_sort:
                resp.append(elements[e])

        return resp


def do_test(i: int, s, n, k, l, r):
    c = Solution()
    resp = c.sortItems(s, n, k, l)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []], [6, 3, 4, 1, 5, 2, 0, 7])
    do_test(1, 8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []], [])


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

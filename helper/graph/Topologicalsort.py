# The function to do Topological Sort.
from typing import Dict, List


def topologicalSort(vertices: int, graph: Dict[int, List[int]]) -> List[int]:
    """Source: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
    Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv,
    vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

    Args:
        vertices (int): number of vertices in a graph. [0 , ..., vertices-1]
        graph (Dict[int, List[int]]): Graph to sort

    Returns:
        List[int]: Topological Sorting
    """

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


def topologicalSort(graph:List[List[int]], indegree:List[int]):
    """Tologlogical sort nodes in graph, return [] if a cycle exists.

    Args:
        graph (List[List[int]]): NxM List. graph[x] - List of childs of node x.
        indegree (List[int]):    indegree[x] - Number of nodes that have a connection to the node x.

    Returns:
        _type_: Tologlogical sort nodes in graph, return [] if a cycle exists
    """
    visited = []
    stack = [node for node in range(len(graph)) if indegree[node] == 0]
    while stack:
        cur = stack.pop()
        visited.append(cur)
        for neib in graph[cur]:
            indegree[neib] -= 1
            if indegree[neib] == 0:
                stack.append(neib)
    return visited if len(visited) == len(graph) else []
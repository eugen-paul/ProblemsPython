from collections import defaultdict
from typing import Deque, Dict, List, Set


def kahnAlgo(n: int, edges: List[List[int]]) -> bool:
    """check if directed graph has a loops

    Args:
        n (int): node count
        edges (List[List[int]]): list of edges

    Returns:
        bool: True - no Loops
             False - has Loops
    """
    graph: Dict[int, Set[int]] = defaultdict(set)

    # the number of edges entering node x
    indegree: List[int] = [0] * n

    for f, t in edges:
        graph[f].add(t)
        indegree[t] += 1

    # node to check for BSF. put all leaf nodes to q (indegree[x] == 0)
    # q: List[int] = [x for x, v in enumerate(indegree) if v == 0]
    q:Deque[int] = Deque([x for x, v in enumerate(indegree) if v == 0])

    nodes_seen = 0
    # loops = set() #<- Nodes that are not a part of a loop and to which no connection from a loop points. However, the connection of the nodes can point to a loop.
    while q:
        node = q.pop()
        nodes_seen += 1
        #loops.add(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return nodes_seen == n


def kahnAlgo_2(n: int, graph: Dict[int, Set[int]]) -> bool:
    """check if directed graph has a loops

    Args:
        n (int): node count
        graph (Dict[int, Set[int]]): 

    Returns:
        bool: True - no Loops
             False - has Loops
    """
    # the number of edges entering node x
    indegree: List[int] = [0] * n

    for vals in graph.values():
        for t in vals:
            indegree[t] += 1

    # node to check for BSF. put all leaf nodes to q (indegree[x] == 0)
    q: List[int] = [x for x, v in enumerate(indegree) if v == 0]

    nodes_seen = 0
    while q:
        node = q.pop(0)
        nodes_seen += 1

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return nodes_seen == n

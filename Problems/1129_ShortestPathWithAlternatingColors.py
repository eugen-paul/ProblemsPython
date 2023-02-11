from typing import Deque, Dict, List, Set


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        dp = [[-1, -1] for _ in range(n)]

        rm: Dict[int, Set[int]] = dict()
        for c in redEdges:
            if c[0] not in rm:
                rm[c[0]] = set()
            rm[c[0]].add(c[1])

        bm: Dict[int, Set[int]] = dict()
        for c in blueEdges:
            if c[0] not in bm:
                bm[c[0]] = set()
            bm[c[0]].add(c[1])

        to_check = Deque()
        # node, color (0-red, 1-blue), cost
        to_check.append((0, 0, 0))
        to_check.append((0, 1, 0))

        while to_check:
            node, color, cost = to_check.popleft()
            if dp[node][color] >= 0 and dp[node][color] <= cost:
                continue
            dp[node][color] = cost
            if color == 0:
                next_nodes = bm.get(node, set())
            else:
                next_nodes = rm.get(node, set())
            for nn in next_nodes:
                to_check.append((nn, (color+1) % 2, cost+1))

        resp = [min(r, b) if r >= 0 and b >= 0 else max(r, b) for r, b in dp]
        return resp


def do_test(i: int, s, n, k, r):
    c = Solution()
    resp = c.shortestAlternatingPaths(s, n, k)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, [[0, 1], [1, 2]], [], [0, 1, -1])
    do_test(1, 3, [[0, 1]], [[2, 1]], [0, 1, -1])
    do_test(2, 3, [[0, 1]], [[1, 2]], [0, 1, 2])

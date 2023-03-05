from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # value to index
        m: Dict[int, Set[int]] = defaultdict(set)

        for i, n in enumerate(arr):
            m[n].add(i)

        visited: List[int] = [inf] * len(arr)

        to_check = Deque()
        to_check.append((0, 0))

        while to_check:
            pos, cost = to_check.popleft()
            if visited[pos] <= cost:
                continue
            visited[pos] = cost

            next_pos = m[arr[pos]]
            # There is no more cheap way to the nodes
            m[arr[pos]] = set()
            if pos > 0:
                next_pos.add(pos-1)
            if pos < len(arr)-1:
                next_pos.add(pos+1)

            for p in next_pos:
                to_check.append((p, cost+1))

        return visited[-1]


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minJumps(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [100, -23, -23, 404, 100, 23, 23, 23, 3, 404], 3)
    do_test(1, [7], 0)
    do_test(2, [7, 6, 9, 6, 9, 6, 9, 7], 1)
    do_test(3, [1, 1, 1, 1, 1, 1, 1, 2], 2)

from collections import defaultdict
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
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

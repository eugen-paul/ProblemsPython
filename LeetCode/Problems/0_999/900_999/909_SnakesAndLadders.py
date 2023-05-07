from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        dest = len(board) * len(board)

        full_map = [0]
        rev = False
        for x in reversed(board):
            if rev:
                full_map.extend(reversed(x))
                rev = False
            else:
                full_map.extend(x)
                rev = True

        visited = set()
        visited.add(1)

        next_check = deque()
        next_check.append((1, 0))

        while len(next_check) > 0:
            n = next_check.popleft()
            pos = n[0]
            if pos == dest:
                return n[1]
            for i in range(1, 7):
                if i + pos > dest:
                    break
                n_pos = i + pos
                if full_map[n_pos] != -1:
                    n_pos = full_map[n_pos]
                if n_pos not in visited:
                    visited.add(n_pos)
                    next_check.append((n_pos, n[1] + 1))

        return -1


def do_test(i: int, s, r):
    c = Solution()
    resp = c.snakesAndLadders(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ], 4)
    do_test(1, [
        [-1, -1],
        [-1, 3]
    ], 1)

from typing import Deque, List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        to_check = Deque()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    to_check.append((x, y, 0))

        if len(to_check) == 0 or len(to_check) == len(grid) * len(grid[0]):
            return -1

        while to_check:
            x, y, cost = to_check.popleft()
            resp = cost
            if x > 0 and grid[y][x-1] == 0:
                to_check.append((x-1, y, cost+1))
                grid[y][x-1] = 1
            if y > 0 and grid[y-1][x] == 0:
                to_check.append((x, y-1, cost+1))
                grid[y-1][x] = 1
            if x < len(grid[0])-1 and grid[y][x+1] == 0:
                to_check.append((x+1, y, cost+1))
                grid[y][x+1] = 1
            if y < len(grid)-1 and grid[y+1][x] == 0:
                to_check.append((x, y+1, cost+1))
                grid[y+1][x] = 1

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxDistance(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    # do_test(0, [[1, 0, 1], [0, 0, 0], [1, 0, 1]], 2)
    # do_test(1, [[1, 0, 0], [0, 0, 0], [0, 0, 0]], 4)
    # do_test(2, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], -1)
    # do_test(3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], -1)
    # do_test(4, [[0]], -1)
    # do_test(5, [[1]], -1)
    do_test(6, [
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]
    ], 2)

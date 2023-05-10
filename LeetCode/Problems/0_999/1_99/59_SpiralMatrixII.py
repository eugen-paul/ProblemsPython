from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        resp = [[0]*n for _ in (range(n))]

        x, y = 0, 0
        v = 1
        d = 0
        steps = 0
        while steps != n*n:
            resp[y][x] = v
            steps += 1
            v += 1
            if d == 0:
                if x < n-1 and resp[y][x+1] == 0:
                    x += 1
                else:
                    y += 1
                    d = 1
            elif d == 1:
                if y < n-1 and resp[y+1][x] == 0:
                    y += 1
                else:
                    x -= 1
                    d = 2
            elif d == 2:
                if x > 0 and resp[y][x-1] == 0:
                    x -= 1
                else:
                    y -= 1
                    d = 3
            else:
                if y > 0 and resp[y-1][x] == 0:
                    y -= 1
                else:
                    x += 1
                    d = 0

        return resp

    def generateMatrix_2(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        resp = [[0 for _ in range(n)] for _ in range(n)]

        x = 0
        y = 0
        r = 0
        count = 1
        while resp[y][x] == 0:
            for _ in range(n - r):
                resp[y][x] = count
                x += 1
                count += 1
            x -= 1
            y += 1

            for _ in range(n - r - 1):
                resp[y][x] = count
                y += 1
                count += 1
            x -= 1
            y -= 1

            for _ in range(n - r - 1):
                resp[y][x] = count
                x -= 1
                count += 1
            x += 1
            y -= 1

            for _ in range(n - r - 2):
                resp[y][x] = count
                y -= 1
                count += 1
            x += 1
            y += 1

            r += 2

        return resp

    def generateMatrix_2(self, n: int) -> List[List[int]]:

        resp = [[0 for _ in range(n)] for _ in range(n)]

        def fill(x: int, y: int, count):
            if x < 0 or x == n or y < 0 or y == n:
                return
            if resp[y][x] != 0:
                return

            resp[y][x] = count

            if y == 0 or (y > 0 and resp[y-1][x] != 0):
                fill(x+1, y, count+1)
            fill(x, y+1, count+1)
            fill(x-1, y, count+1)
            fill(x, y-1, count+1)

        fill(0, 0, 1)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.generateMatrix(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    do_test(1, 1, [[1]])
    do_test(2, 4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])

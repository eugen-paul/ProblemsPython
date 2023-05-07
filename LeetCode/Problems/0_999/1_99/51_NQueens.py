from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        resp: List[List[str]] = []

        area: List[List[str]] = [["." for _ in range(n)] for _ in range(n)]

        def is_ok(x: int, y: int) -> bool:
            for row in range(y):
                if area[row][x] == "Q":
                    return False

                if x - (y-row) >= 0 and area[row][x - (y-row)] == "Q":
                    return False

                if x + (y-row) < n and area[row][x + (y-row)] == "Q":
                    return False

            return True

        def set_queen(rest_pos: Set[int], rest_n: int):
            if len(rest_pos) == 0:
                a: List[str] = ["".join(row) for row in area]
                resp.append(a)
                return

            for i in rest_pos:
                pos_x = i
                pos_y = n-len(rest_pos)

                area[pos_y][pos_x] = "Q"

                if not is_ok(pos_x, pos_y):
                    area[pos_y][pos_x] = "."
                    continue

                sub_rest_pos = set(rest_pos)
                sub_rest_pos.remove(i)
                set_queen(sub_rest_pos, rest_n - 1)
                area[pos_y][pos_x] = "."

        col = set(range(n))

        set_queen(col, n)

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.solveNQueens(s)
    resp.sort()
    r.sort()
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."]
    ])
    do_test(1, 1, [
        ["Q"]
    ])

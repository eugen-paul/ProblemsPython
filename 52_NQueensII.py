from typing import List, Set


class Solution:
    def totalNQueens(self, n: int) -> int:
        resp: List[List[int]] = []
        area: List[int] = [None] * n

        def is_ok(x: int, y: int) -> bool:
            for row in range(y):
                if area[row] == x - (y-row) or area[row] == x + (y-row):
                    return False
            return True

        def set_queen(rest_pos: Set[int], rest_n: int):
            if len(rest_pos) == 0:
                a: List[int] = area.copy()
                resp.append(a)
                return

            for i in rest_pos:
                pos_x = i
                pos_y = n-len(rest_pos)

                area[pos_y] = i

                if not is_ok(pos_x, pos_y):
                    continue

                sub_rest_pos = set(rest_pos)
                sub_rest_pos.remove(i)
                set_queen(sub_rest_pos, rest_n - 1)

        col = set(range(n))

        set_queen(col, n)

        return len({"".join(str(row)) for row in resp})


def do_test(i: int, s, r):
    c = Solution()
    resp = c.totalNQueens(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, 2)
    do_test(1, 1, 1)

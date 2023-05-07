from typing import Dict, List, Set, Tuple


class Solution:
    """ 
    pos - Listing of all possible numbers (value) that can occur at a position (key).
    """

    def delete_check_value(self, pos: Dict[Tuple[int, int], Set[int]], x, y, w, h, v):
        for i in range(x, x+w):
            for j in range(y, y+h):
                if (i, j) in pos:
                    s = pos[(i, j)]
                    if v in s:
                        s.remove(v)

    def delete_unpossible(self, pos: Dict[Tuple[int, int], Set[int]], p, v) -> None:
        """
        Cleans up the "pos". Deletes from the list of possible numbers (value of pos) the numbers that can no longer occur (v).
        """
        self.delete_check_value(pos, 0, p[1], 9, 1, v)
        self.delete_check_value(pos, p[0], 0, 1, 9, v)
        mr = p[0] // 3
        mc = p[1] // 3
        self.delete_check_value(pos, mr * 3, mc * 3, 3, 3, v)

    def is_single(self, pos: Dict[Tuple[int, int], Set[int]], x, y, w, h, v) -> bool:
        found = False
        for i in range(x, x+w):
            for j in range(y, y+h):
                if (i, j) in pos:
                    s = pos[(i, j)]
                    if v in s:
                        if found:
                            return False
                        found = True
        return True

    def check_unique(self, pos: Dict[Tuple[int, int], Set[int]]):
        for p, v_set in pos.items():
            for v in v_set:
                mr = p[0] // 3
                mc = p[1] // 3

                if self.is_single(pos, 0, p[1], 9, 1, v) \
                    or self.is_single(pos, p[0], 0, 1, 9, v) \
                        or self.is_single(pos, mr * 3, mc * 3, 3, 3, v):
                    v_set.clear()
                    self.delete_check_value(pos, 0, p[1], 9, 1, v)
                    self.delete_check_value(pos, p[0], 0, 1, 9, v)
                    self.delete_check_value(pos, mr * 3, mc * 3, 3, 3, v)
                    v_set.add(v)
                    break

    def solve(self, next_check: Dict[Tuple[int, int], int], pos: Dict[Tuple[int, int], Set[int]], m: Dict[Tuple[int, int], int]) -> bool:
        """
        next_check - Listing of known numbers that have not yet been viewed.
        """
        def is_single(x, y, w, h, v) -> bool:
            found = False
            for i in range(x, x+w):
                for j in range(y, y+h):
                    if (i, j) in m:
                        s = m[(i, j)]
                        if v == s:
                            if found:
                                return False
                            found = True
            return True

        while len(next_check) != 0:
            # Edit the list of possible numbers. Delete from the list all numbers that are already known or numbers that cannot occur.
            for p, v in next_check.items():
                self.delete_unpossible(pos, p, v)
            next_check.clear()
            self.check_unique(pos)

            to_remove = set()

            # Check if, after processing, there are positions where only one number can appear. If yes, then add the position to next_check
            for p, s in pos.items():
                if len(s) == 1:
                    next_check[p] = s.pop()
                    m[p] = next_check[p]

                    # Here you have to make sure that if you add a number to the result, that the result remains valid.
                    unique_r = is_single(0, p[1], 9, 1, next_check[p])
                    unique_c = is_single(p[0], 0, 1, 9, next_check[p])
                    mr = p[0] // 3
                    mc = p[1] // 3
                    unique_s = is_single(mr * 3, mc * 3, 3, 3, next_check[p])
                    if not unique_r or not unique_c or not unique_s:
                        return False

                    to_remove.add(p)
                elif len(s) == 0:
                    return False
            for p in to_remove:
                pos.pop(p)

        return True

    def rec_solver(self, next_check: Dict[Tuple[int, int], int], pos: Dict[Tuple[int, int], Set[int]], m: Dict[Tuple[int, int], int]) -> bool:
        is_ok = self.solve(next_check, pos, m)
        if not is_ok:
            return False

        if len(pos) == 0:
            return True

        # No solution could be found. Find a position where the number of possible numbers is the smallest.
        min_tries_k = None
        min_tries_l = 10
        for k_main, v_main in pos.items():
            if len(v_main) < min_tries_l:
                min_tries_l = len(v_main)
                min_tries_k = k_main
                if min_tries_l == 2:
                    break

        # Try the numbers one after the other.
        for v_try in pos[min_tries_k]:
            m_sub = m.copy()
            m_sub[k_main] = v_try

            pos_sub: Dict[Tuple[int, int], Set[int]] = dict()
            for k, v in pos.items():
                pos_sub[k] = v.copy()
            pos_sub.pop(k_main)
            next_check_sub = next_check.copy()
            next_check_sub[k_main] = v_try

            # Recursive call on itself. Use the copies of the input data.
            is_ok = self.rec_solver(next_check_sub, pos_sub, m_sub)
            if is_ok:
                break

        if is_ok:
            # A solution was found. Copy the data from the temporary storage to the input listing.
            m.clear()
            for k, v in m_sub.items():
                m[k] = v
            return True

        # impossible variant. Return False.
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        m: Dict[Tuple[int, int], int] = dict()
        next_check: Dict[Tuple[int, int], int] = dict()
        pos: Dict[Tuple[int, int], Set[int]] = dict()
        s = set()

        for x in range(9):
            for y in range(9):
                if board[y][x] != '.':
                    m[(x, y)] = int(board[y][x])
                    next_check[(x, y)] = int(board[y][x])
                else:
                    s.add((x, y))
                    pos[(x, y)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        if len(pos) != 0:
            self.rec_solver(next_check, pos, m)

        for p, z in m.items():
            board[p[1]][p[0]] = str(z)


def do_test(i: int, s, r):
    c = Solution()
    resp = c.solveSudoku(s)
    if s == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", s)


if __name__ == "__main__":
    do_test(0, [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ],
        [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ])

    do_test(1, [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."]
    ],
        [
        ["5", "1", "9", "7", "4", "8", "6", "3", "2"],
        ["7", "8", "3", "6", "5", "2", "4", "1", "9"],
        ["4", "2", "6", "1", "3", "9", "8", "7", "5"],
        ["3", "5", "7", "9", "8", "6", "2", "4", "1"],
        ["2", "6", "4", "3", "1", "7", "5", "9", "8"],
        ["1", "9", "8", "5", "2", "4", "3", "6", "7"],
        ["9", "7", "5", "8", "6", "3", "1", "2", "4"],
        ["8", "3", "2", "4", "9", "1", "7", "5", "6"],
        ["6", "4", "1", "2", "7", "5", "9", "8", "3"]
    ])

    do_test(2, [
        [".", ".", ".", "2", ".", ".", ".", "6", "3"],
        ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
        [".", ".", "1", ".", ".", "3", "9", "8", "."],
        [".", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "3", "8", ".", ".", "."],
        [".", "3", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", "6", "3", ".", ".", "5", ".", "."],
        ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
        ["4", "7", ".", ".", ".", "1", ".", ".", "."]
    ],
        [
        ["8", "5", "4", "2", "1", "9", "7", "6", "3"],
        ["3", "9", "7", "8", "6", "5", "4", "2", "1"],
        ["2", "6", "1", "4", "7", "3", "9", "8", "5"],
        ["7", "8", "5", "1", "2", "6", "3", "9", "4"],
        ["6", "4", "9", "5", "3", "8", "1", "7", "2"],
        ["1", "3", "2", "9", "4", "7", "8", "5", "6"],
        ["9", "2", "6", "3", "8", "4", "5", "1", "7"],
        ["5", "1", "3", "7", "9", "2", "6", "4", "8"],
        ["4", "7", "8", "6", "5", "1", "2", "3", "9"]
    ])

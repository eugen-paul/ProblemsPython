from typing import Counter, List, Set, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def check(start_x: int, start_y: int) -> bool:

            to_check: List[Tuple[int, int, int, List[bool]]] = [(start_x, start_y, 1, [False]*36)]

            while to_check:
                x, y, l, visited = to_check.pop()
                if x < 0 or y < 0 or y >= len(board) or x >= len(board[0]):
                    continue

                pos = len(board[0]) * y + x
                if visited[pos]:
                    continue

                if board[y][x] != word[l-1]:
                    continue

                if l == len(word) and board[y][x] == word[l-1]:
                    return True

                visited[pos] = True

                to_check.append((x+1, y, l+1, visited))
                to_check.append((x-1, y, l+1, visited.copy()))
                to_check.append((x, y+1, l+1, visited.copy()))
                to_check.append((x, y-1, l+1, visited.copy()))

            return False

        wc = Counter(word)
        mc = Counter()
        for row in board:
            for c in row:
                mc[c] += 1

        d = wc - mc
        if len(d) > 0:
            return False

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0] and check(x, y):
                    return True

        return False

    def exist_1(self, board: List[List[str]], word: str) -> bool:

        def check(start_x: int, start_y: int) -> bool:

            to_check: List[Tuple[int, int, int, Set[Tuple[int, int]]]] = [(start_x, start_y, 1, set())]

            while to_check:
                x, y, l, visited = to_check.pop()
                if (x, y) in visited:
                    continue

                if x < 0 or y < 0 or y >= len(board) or x >= len(board[0]):
                    continue

                if board[y][x] != word[l-1]:
                    continue

                if l == len(word) and board[y][x] == word[l-1]:
                    return True

                visited.add((x, y))

                to_check.append((x+1, y, l+1, visited))
                to_check.append((x-1, y, l+1, visited.copy()))
                to_check.append((x, y+1, l+1, visited.copy()))
                to_check.append((x, y-1, l+1, visited.copy()))

            return False

        wc = Counter(word)
        mc = Counter()
        for row in board:
            for c in row:
                mc[c] += 1

        d = wc - mc
        if len(d) > 0:
            return False

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0] and check(x, y):
                    return True

        return False


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.exist(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True)
    do_test(1, [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True)
    do_test(2, [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False)
    do_test(3, [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "A", True)
    do_test(4, [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS", True)
    do_test(5, [["A", "B"], ["C", "D"]], "ACDB", True)

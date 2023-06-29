from collections import defaultdict
from functools import cache
from math import inf
import math
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        h = len(grid)
        w = len(grid[0])
        A,Z = ord("A"), ord("Z")

        start = None
        keys: Dict[Tuple[int, int], int] = dict()
        m = [[-1] * w for _ in range(h)]

        for r in range(h):
            for c in range(w):
                p: str = grid[r][c]
                if p == "@":
                    start = (c, r)
                    m[r][c] = 0
                elif p >= "a" and p <= "z":
                    keys[(c, r)] = ord(p.upper())
                    m[r][c] = 0
                elif p >= "A" and p <= "Z":
                    m[r][c] = ord(p.upper())
                elif p == ".":
                    m[r][c] = 0
                else:
                    m[r][c] = -1

        @cache
        def get_way(start, end, keys) -> int:
            q = Deque()
            q.append((start[0], start[1], 0))

            SEEN = [[False] * w for _ in range(h)]
            while q:
                cur_x, cur_y, way = q.popleft()
                if (cur_x, cur_y) == end:
                    return way
                for x, y in get_nb(cur_x, cur_y, w-1, h-1):
                    if m[y][x] == -1:
                        continue
                    if m[y][x] >= A and m[y][x] <= Z and m[y][x] not in keys:
                        continue
                    if SEEN[y][x]:
                        continue
                    SEEN[y][x] = True
                    q.append((x, y, way+1))

            return -1

        @cache
        def get_full_way(start: Tuple[int, int], rest: Set[Tuple[int, int]]) -> int:
            if len(rest) == 0:
                return 0

            my_key = keys.copy()
            for x, y in rest:
                my_key.pop((x, y))
            my_key = frozenset(my_key.values())

            best = inf
            for nxt in rest:
                to_nxt = get_way(start, nxt, my_key)
                if to_nxt == -1:
                    continue
                other = get_full_way(nxt, rest-{nxt})
                if other == -1:
                    continue
                best = min(best, other + to_nxt)

            return best if best != inf else -1

        resp = get_full_way(start, frozenset(keys.keys()))
        return resp if resp != inf else -1


def do_test(i: int, s, r):
    c = Solution()
    resp = c.shortestPathAllKeys(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["@.a..", "###.#", "b.A.B"], 8)
    do_test(1, ["@..aA", "..B#.", "....b"], 6)
    do_test(2, ["@Aa"], -1)
    do_test(3,
            [
                "#..#.#.#..#.#.#.....#......#..",
                ".#.......#....#A.....#.#......",
                "#....#.....#.........#........",
                "...#.#.........#..@....#....#.",
                ".#.#.##...#.........##....#..#",
                "..........#..#..###....##..#.#",
                ".......#......#...#...#.....c#",
                ".#...#.##......#...#.###...#..",
                "..........##...#.......#......",
                "#...#.........a#....#.#.##....",
                "..#..#...#...#..#....#.....##.",
                "..........#...#.##............",
                "...#....#..#.........#..D.....",
                "....#E.#....##................",
                "...........##.#.......#.#....#",
                "...#..#...#.#............#e...",
                "..#####....#.#...........##..#",
                "##......##......#.#...#..#.#..",
                ".#F.......#..##.......#....#..",
                "............#....#..#..#...#..",
                ".............#...#f...#..##...",
                "....#..#...##.........#..#..#.",
                ".....#.....##.###..##.#......#",
                ".#..#.#...#.....#........###..",
                ".....#.#...#...#.....#.....#..",
                "##.....#....B.....#..#b.......",
                ".####....##..#.##..d.#......#.",
                "..#.....#....##........##...##",
                "...#...#...C..#..#....#.......",
                "#.....##.....#.#......#......."
            ], 70)

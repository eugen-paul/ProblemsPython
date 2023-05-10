from typing import Deque, List, Tuple


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            yield (xn, yn)


for _ in range(int(input())):
    h, w = i_array_int()
    a = [list(map(int, input().split())) for _ in range(h)]

    d = []
    best = 0
    for r in range(h):
        for c in range(w):
            if a[r][c] == 0:
                continue
            d = Deque()
            d.append((c, r))

            s = a[r][c]
            a[r][c] = 0
            while d:
                x, y = d.pop()
                for nx, ny in get_nb(x, y, w-1, h-1):
                    if a[ny][nx] == 0:
                        continue
                    s += a[ny][nx]
                    a[ny][nx] = 0
                    d.append((nx, ny))
            best = max(best, s)
    print(best)

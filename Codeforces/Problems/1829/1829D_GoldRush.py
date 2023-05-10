from typing import Deque, List


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    n, m = i_array_int()

    d = Deque()
    d.append(n)

    seen = set()
    ok = False
    while d:
        p = d.popleft()
        if p == m:
            ok = True
            break
        if p < m or p % 3 != 0 or p in seen:
            continue
        seen.add(p)
        d.append(p // 3)
        d.append((p // 3) * 2)
    if ok:
        print("YES")
    else:
        print("NO")

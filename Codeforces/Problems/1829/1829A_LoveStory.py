from typing import List


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


for _ in range(int(input())):
    a = input()
    c = "codeforces"
    d = 0
    for k, l in zip(a, c):
        if k != l:
            d += 1
    print(d)

# for _ in range(int(input())):
#     a = input()
#     c = "codeforces"
#     print(sum(a != b for a,b in zip(a,c)))

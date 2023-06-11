from typing import List, Tuple


def v1(magic_number: int):
    l, r = 1, 1_000_000
    while l < r:          # until l < r
        m = (r+l+1) // 2  # compute "+1" when comparing with ">=" / < in the first if-query.
        if magic_number >= m:  # <------
            l = m
        else:
            r = m-1
    return l


def bs_a(a: List[int], v: int):
    l, r = 0, len(a)-1
    while l < r:
        m = (r+l+1) // 2
        if v >= a[m]:
            l = m
        else:
            r = m-1
    return l


def bs_right_a(a: List[Tuple[int, int]], v: int):
    """ The return position i is such that all e in a[:i+1] have e <= x. All a[i+1:] have e > x. """
    l, r = 0, len(a)-1
    while l <= r:
        m = (r+l) // 2
        if v >= a[m][0]:
            l = m + 1
        else:
            r = m - 1
    return l-1


def v2(magic_number: int) -> int:
    l, r = 1, 1_000_000
    while l <= r:         # until l <= r
        m = (r+l) // 2    # compute "+0" when comparing with ">" / "<=" in the first if-query.
        if magic_number > m:  # <------
            l = m+1
        else:
            r = m-1
    return l


if __name__ == "__main__":
    for i in range(1, 100_000):
        if i != v1(i):
            print("error 1:", i)
        if i != v2(i):
            print("error 2:", i)

    a = [(0, 0), (1, 1), (2, 2), (4, 4), (5, 5), (7, 7), (10, 10), (12, 12)]
    for n in a:
        if a[bs_right_a(a, n[0])][1] != n[1]:
            print("bs_right_a error ", n)

def v1(magic_number: int):
    l, r = 1, 1_000_000
    while l < r:          # until l < r
        m = (r+l+1) // 2  # compute "+1" when comparing with ">=" / < in the first if-query.
        if magic_number >= m:  # <------
            l = m
        else:
            r = m-1
    return l


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
        if i != v1(i): print("error 1:", i)
        if i != v2(i): print("error 2:", i)
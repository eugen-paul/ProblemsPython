from functools import cmp_to_key
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat = [(sum(r), i) for i, r in enumerate(mat)]
        mat.sort()
        return [i for _, i in mat[:k]]

    def kWeakestRows_q(self, mat: List[List[int]], k: int) -> List[int]:
        t = list()
        for i, e in enumerate(mat):
            t.append((i, sum(e)))

        def s_func(a, b):
            if a[1] != b[1]:
                return a[1] - b[1]
            return a[0] - b[0]

        t.sort(key=cmp_to_key(s_func))

        return [x[0] for x in t[:k]]


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.kWeakestRows(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ], 3, [2, 0, 3])
    do_test(1, [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ], 2, [0, 2])

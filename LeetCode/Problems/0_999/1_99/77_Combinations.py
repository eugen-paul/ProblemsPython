import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """need too much memory"""
        resp = []
        for i in range(1, n+1):
            resp += [[i] + r for r in resp if len(r) <= k-1]
            resp += [[i]]

        return [sorted(r) for r in resp if len(r) == k]

    def combine_3(self, n: int, k: int) -> List[List[int]]:
        return [list(i) for i in itertools.combinations(range(1, n+1), k)]

    def combine_2(self, n: int, k: int) -> List[List[int]]:
        def solve(s: List[int], k) -> List[List[int]]:
            if k == len(s):
                return [s[:]]
            resp = solve(s[1:], k)
            if k >= 1:
                resp.extend([[s[0]] + sub for sub in solve(s[1:], k-1)])
            return resp

        return solve([i for i in range(1, n+1)], k)

    def combine_1(self, n: int, k: int) -> List[List[int]]:
        def rec(start: int, rest_k: int) -> List[List[int]]:
            if rest_k == 1:
                return [[x] for x in range(start, n+1)]

            r = list()
            for i in range(start, n - rest_k + 2):
                r += [[i] + x for x in rec(i+1, rest_k-1)]

            return r

        return rec(1, k)

    def combine_1(self, n: int, k: int) -> List[List[int]]:
        s = [*range(1, n+1)]

        def rec(rest_n: List[int], rest_k: int) -> List[List[int]]:
            if rest_k == 1:
                return [[x] for x in rest_n]

            r = list()
            for i in range(len(rest_n) - rest_k + 1):
                r += [[rest_n[i]] + x for x in rec(rest_n[i+1:], rest_k-1)]

            return r

        return rec(s, k)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.combine(s, n)
    resp.sort()
    r.sort()
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    do_test(1, 1, 1, [[1]])
    do_test(2, 5, 3, [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]])
    do_test(3, 5, 4, [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]])
    do_test(4, 6, 3, [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 3, 4], [1, 3, 5],
                      [1, 3, 6], [1, 4, 5], [1, 4, 6], [1, 5, 6], [2, 3, 4], [2, 3, 5],
                      [2, 3, 6], [2, 4, 5], [2, 4, 6], [2, 5, 6], [3, 4, 5], [3, 4, 6], [3, 5, 6], [4, 5, 6]])

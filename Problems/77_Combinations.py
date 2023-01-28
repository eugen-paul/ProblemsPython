from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
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
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    do_test(1, 1, 1, [[1]])

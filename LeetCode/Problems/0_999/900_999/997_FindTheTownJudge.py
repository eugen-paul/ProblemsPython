from collections import Counter
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        r1 = Counter()
        r2: set = set(range(1, n+1))
        for i, k in trust:
            r2.discard(i)
            r1[k] += 1

        for i in r2:
            if r1.get(i, 0) == n - 1:
                return i

        return -1

    def findJudge_slow(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1

        r1 = Counter()
        r2: set = set()
        for i, k in trust:
            r2.add(i)
            r1[k] += 1

        for k, v in r1.items():
            if v == n-1 and k not in r2:
                return k
        return -1


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.findJudge(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 2, [[1, 2]], 2)
    do_test(1, 3, [[1, 3], [2, 3]], 3)
    do_test(2, 3, [[1, 3], [2, 3], [3, 1]], -1)
    do_test(3, 1, [], 1)
    do_test(4, 2, [], -1)

from typing import List, Dict, Tuple, Counter


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1, len(triangle)):
            triangle[r][0] += triangle[r-1][0]
            for i in range(1, r):
                triangle[r][i] += min(triangle[r-1][i-1], triangle[r-1][i])
            triangle[r][-1] += triangle[r-1][-1]

        return min(triangle[-1])


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minimumTotal(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11)
    do_test(1, [[-10]], -10)

import heapq
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        q: List[(int, int)] = list()
        heapq.heapify(q)

        max_sq = 0

        for i, n in enumerate(heights):
            if len(q) == 0:
                if n > 0:
                    heapq.heappush(q, (10000 - n, n, i))
            else:
                start_pos = i
                while q:
                    max_el = heapq.heappop(q)
                    if max_el[1] < n:
                        heapq.heappush(q, max_el)
                        break
                    max_sq = max(max_sq, max_el[1] * (i - max_el[2]))
                    start_pos = min(start_pos, max_el[2])
                if n > 0:
                    heapq.heappush(q, (10000 - n, n, start_pos))

        i = len(heights)
        while q:
            max_el = heapq.heappop(q)
            max_sq = max(max_sq, max_el[1] * (i - max_el[2]))

        return max_sq


def do_test(i: int, s, r):
    c = Solution()
    resp = c.largestRectangleArea(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [2, 1, 5, 6, 2, 3], 10)
    do_test(1, [2, 4], 4)
    do_test(2, [2, 1, 5, 1, 2, 3], 6)
    do_test(3, [0, 0, 5, 0, 0, 3], 5)
    do_test(4, [0, 0, 2, 0, 0, 0], 2)

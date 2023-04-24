from bisect import bisect_left, bisect_right
from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        count = Counter()
        points = []
        heapq.heapify(points)
        last_heights = []
        heapq.heapify(last_heights)
        resp = []

        for l, r, h in buildings:
            heapq.heappush(points, (l, h, 1))
            heapq.heappush(points, (r, h, 0))

        last_x = -1
        last_max_h = -1
        while points:
            x, h, d = heapq.heappop(points)
            if d == 1:
                # start of the building
                count[h] += 1
                heapq.heappush(last_heights, -h)
                if last_max_h < h:
                    last_max_h = h
                    if last_x != x:
                        resp.append([x, last_max_h])
                    else:
                        # if x-coordinate has not changed, then assume the maximum height.
                        resp[-1] = [x, last_max_h]
                    last_x = x
            else:
                # end of the building
                count[h] -= 1
                if last_heights[0] == -h:
                    # the building with the maximum height was deleted.
                    last_max_h = 0
                    while last_heights:
                        last_max_h = - last_heights[0]
                        if count[last_max_h] == 0:
                            # the next possible maximum height no longer exists.
                            heapq.heappop(last_heights)
                            last_max_h = 0
                        else:
                            last_max_h = - last_heights[0]
                            break
                    if last_x != x:
                        resp.append([x, last_max_h])
                    else:
                        # if x-coordinate has not changed, then assume the maximum height.
                        resp[-1] = [x, last_max_h]
                    last_x = x

        # delete points that lie on the same line.
        resp1 = []
        last_h = -1
        for x, h in resp:
            if last_h != h:
                resp1.append([x, h])
                last_h = h

        return resp1

    def getSkyline_i(self, buildings: List[List[int]]) -> List[List[int]]:
        """internet solution:
        https://leetcode.com/problems/the-skyline-problem/solutions/2997005/solution/
        """
        if len(buildings) == 0:
            return []

        buildings.sort(key=lambda v: v[2])
        pos, height = [0], [0]
        for left, right, h in buildings:
            i = bisect_left(pos, left)
            j = bisect_right(pos, right)
            height[i:j] = [h, height[j-1]]
            pos[i:j] = [left, right]
        res = []
        prev = 0
        for v, h in zip(pos, height):
            if h != prev:
                res.append([v, h])
                prev = h

        return res

    def getSkyline_i(self, buildings: List[List[int]]) -> List[List[int]]:
        """internet solution:
        https://leetcode.com/problems/the-skyline-problem/solutions/2642224/python-two-heaps-to-maintain-the-max-height/
        """
        change_point = []
        for start, end, height in buildings:
            # 1 means the start of the building
            # -1 means the end of the building
            change_point.append([start, 1, height])
            change_point.append([end, -1, height])
        change_point.sort(key=lambda x: [x[0], -x[1], -x[2]])
        res = []
        heap = []  # height
        remove_heap = []
        for i, (position, flag, height) in enumerate(change_point):
            # add a building
            if flag == 1:
                heapq.heappush(heap, -height)
            # remove a building
            else:
                heapq.heappush(remove_heap, -height)
            # remove all the removed height, to avoid taking the removed height as the highest
            while len(remove_heap) > 0 and heap[0] == remove_heap[0]:
                heapq.heappop(heap)
                heapq.heappop(remove_heap)
            # no building at the current position
            if len(heap) == 0:
                res.append([position, 0])
            else:
                # take consideration of the first and the last one
                # if the current max height equals the last height(two adjacent buildings), continue
                # if the current position has multiple operations(only take the highest one), continue
                if i == 0 or i == len(change_point)-1 or (-heap[0] != res[-1][1] and position != change_point[i+1][0]):
                    res.append([position, -heap[0]])  # current max height
        return res


def do_test(i: int, s, r):
    c = Solution()
    resp = c.getSkyline(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0,
            [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
    do_test(1, [[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]])

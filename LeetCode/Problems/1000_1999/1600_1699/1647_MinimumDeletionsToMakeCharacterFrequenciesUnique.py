from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        cnt = list([-i for i in cnt.values()])
        heapq.heapify(cnt)
        resp = 0
        last = -inf
        while cnt:
            cur = heapq.heappop(cnt)
            if last < cur or cur == 0:
                last = cur
            else:
                resp += 1
                heapq.heappush(cnt, cur+1)

        return resp

    def minDeletions_i(self, s: str) -> int:
        """internet solution:
        https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/solutions/4033205/98-18-greedy-heap-sorting/?envType=daily-question&envId=2023-09-12
        """
        cnt = Counter(s)
        deletions = 0
        used_frequencies = set()

        for _, freq in cnt.items():
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                deletions += 1
            used_frequencies.add(freq)

        return deletions


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minDeletions(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "aab", 0)
    do_test(1, "aaabbbcc", 2)
    do_test(2, "ceabaacb", 2)
    do_test(3, "bbcebab", 2)


def get_nb(x: int, y: int, maxX: int, maxY: int, minX: int = 0, minY: int = 0, dia: bool = False) -> List[Tuple[int, int]]:
    resp = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if dia:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        xn, yn = x+dx, y+dy
        if minX <= xn <= maxX and minY <= yn <= maxY:
            resp.append((xn, yn))
    return resp

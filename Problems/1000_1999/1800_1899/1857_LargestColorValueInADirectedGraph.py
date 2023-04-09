from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

import sys
sys.setrecursionlimit(100000)


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        roots = set(range(len(colors)))
        g = defaultdict(set)
        for f, t in edges:
            g[f].add(t)
            roots.discard(t)
        if len(roots) == 0:
            return -1

        visited = set()
        checking = set()

        def get_color_count(m: Dict[int, int], node: int, color: str) -> int:
            if node in checking:
                raise Exception
            if node in m:
                return m[node]

            visited.add(node)
            resp = 1 if colors[node] == color else 0

            best = 0
            checking.add(node)
            for nxt in g[node]:
                best = max(best, get_color_count(m, nxt, color))
            checking.discard(node)

            m[node] = best + resp
            return best + resp

        try:
            resp = 0
            for color in set(colors):
                m: Dict[int, int] = dict()
                for root in roots:
                    resp = max(resp, get_color_count(m, root, color))
        except Exception:
            return -1

        if len(visited) != len(colors):
            return -1
        return resp

    def largestPathValue_s2(self, colors: str, edges: List[List[int]]) -> int:
        """faster but still too slow"""
        roots = set(range(len(colors)))
        g = defaultdict(set)
        for f, t in edges:
            g[f].add(t)
            roots.discard(t)
        if len(roots) == 0:
            return -1

        visited = set()

        resp = 0
        for root in roots:
            d: Deque[Tuple[int, Set[int], Counter]] = Deque()
            d.append((root, set(), Counter()))
            sub_vis: Dict[int, List[Counter]] = defaultdict(list)

            while d:
                node, path, cnt = d.pop()
                visited.add(node)
                if node in path:
                    return -1
                cnt[colors[node]] += 1
                if node in sub_vis:
                    is_new = True
                    for sub_cnt in sub_vis[node]:
                        if cnt <= sub_cnt:
                            is_new = False
                            break
                    if not is_new:
                        continue
                path.add(node)
                sub_vis[node].append(cnt)
                if node not in g:
                    resp = max(resp, cnt.most_common(1)[0][1])
                else:
                    for nxt in g[node]:
                        d.append((nxt, set(path), Counter(cnt)))
        if len(visited) != len(colors):
            return -1
        return resp

    def largestPathValue_s(self, colors: str, edges: List[List[int]]) -> int:
        """too slow"""
        roots = set(range(len(colors)))
        g = defaultdict(set)
        for f, t in edges:
            g[f].add(t)
            roots.discard(t)
        if len(roots) == 0:
            return -1

        visited = set()

        def comp_cost(s: Set[int]) -> int:
            cnt = Counter()
            for n in s:
                cnt[colors[n]] += 1
            return cnt.most_common(1)[0][1]

        resp = 0
        for root in roots:
            d: Deque[Tuple[int, Set[int]]] = Deque()
            d.append((root, set()))

            while d:
                node, path = d.popleft()
                visited.add(node)
                if node in path:
                    return -1
                path.add(node)
                if node not in g:
                    resp = max(resp, comp_cost(path))
                else:
                    for nxt in g[node]:
                        d.append((nxt, set(path)))
        if len(visited) != len(colors):
            return -1
        return resp


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.largestPathValue(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "abaca", [[0, 1], [0, 2], [2, 3], [3, 4]], 3)
    do_test(1, "a", [[0, 0]], -1)
    do_test(2, "ab", [[0, 1], [1, 1]], -1)
    do_test(3, "iivvvvv", [[0, 1], [1, 2], [1, 3], [2, 3], [3, 4], [2, 4], [3, 5], [1, 5], [4, 5], [5, 6]], 5)
    do_test(4, "qddqqqddqqdqddddddqdqqddddqdqdqqdddqddqdqqdqqqqqddqddqqddqqqdqqqqdqdddddqdq",
            [
                [0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [4, 5], [3, 6], [5, 6],
                [6, 7], [5, 7], [3, 7], [6, 8], [5, 8], [4, 8], [8, 9], [9, 10],
                [10, 11], [9, 11], [9, 12], [11, 12], [6, 12], [11, 13], [9, 13],
                [13, 14], [12, 14], [10, 14], [11, 14], [13, 15], [14, 15],
                [12, 16], [9, 16], [7, 16], [15, 17], [13, 17], [17, 18], [11, 18],
                [17, 19], [18, 19], [13, 19], [17, 20], [18, 20], [19, 21],
                [17, 21], [12, 22], [21, 22], [16, 22], [22, 23], [21, 23],
                [16, 24], [22, 24], [15, 25], [24, 25], [20, 25], [12, 25],
                [23, 26], [26, 27], [13, 27], [27, 28], [21, 28], [26, 28],
                [28, 29], [15, 30], [27, 30], [24, 30], [21, 30], [27, 31],
                [30, 31], [25, 32], [29, 32], [17, 33], [31, 33], [32, 33],
                [25, 34], [33, 35], [31, 35], [34, 35], [30, 36], [35, 37],
                [36, 37], [26, 38], [36, 38], [34, 38], [37, 38], [38, 39],
                [22, 39], [39, 40], [40, 41], [38, 41], [20, 41], [41, 42],
                [37, 42], [40, 43], [42, 43], [43, 44], [41, 44], [32, 44],
                [38, 44], [39, 44], [43, 45], [44, 45], [44, 46], [45, 46],
                [45, 47], [42, 47], [43, 48], [45, 49], [45, 50], [48, 51],
                [30, 51], [46, 52], [48, 52], [38, 52], [51, 52], [47, 53],
                [45, 53], [53, 54], [48, 54], [30, 54], [50, 55], [30, 55],
                [36, 55], [55, 56], [39, 56], [54, 56], [50, 57], [56, 58],
                [32, 58], [57, 59], [49, 59], [38, 60], [60, 61], [35, 61],
                [54, 61], [53, 61], [54, 62], [58, 62], [62, 63], [40, 63],
                [58, 63], [49, 64], [63, 64], [47, 64], [39, 64], [45, 64],
                [62, 65], [64, 65], [54, 65], [52, 66], [61, 66], [60, 66],
                [55, 67], [65, 67], [45, 68], [56, 68], [36, 68], [67, 69],
                [66, 69], [27, 70], [60, 70], [67, 70], [48, 71], [70, 71],
                [53, 71], [62, 72], [72, 73], [73, 74]
            ],
            26)
    do_test(5, "keitgkggegyktyeytgyigkggktiigigkeyygtgytiygtkg",
            [
                [0, 1], [1, 2], [2, 3], [1, 3], [3, 4], [4, 5], [5, 6], [3, 6], [5, 7],
                [6, 8], [5, 8], [7, 8], [8, 9], [7, 10], [8, 10], [9, 10], [10, 11],
                [9, 11], [7, 11], [5, 12], [11, 12], [11, 13], [13, 14], [12, 14],
                [12, 15], [10, 15], [14, 15], [7, 15], [9, 16], [13, 16], [12, 16],
                [15, 16], [11, 17], [14, 17], [16, 17], [15, 18], [14, 18], [17, 18],
                [18, 19], [14, 19], [13, 19], [14, 20], [15, 21], [12, 21], [20, 21],
                [19, 22], [20, 22], [21, 22], [22, 23], [19, 23], [11, 23], [18, 23],
                [13, 24], [23, 24], [21, 24], [24, 25], [13, 25], [23, 25], [15, 26],
                [23, 26], [25, 26], [24, 26], [26, 27], [25, 27], [26, 28], [27, 28],
                [20, 28], [23, 28], [11, 28], [23, 29], [29, 30], [25, 31], [26, 31],
                [15, 32], [30, 32], [31, 33], [27, 33], [30, 33], [28, 33], [29, 34],
                [32, 35], [33, 35], [34, 35], [35, 36], [13, 36], [34, 36], [30, 37],
                [36, 37], [35, 37], [24, 37], [35, 38], [34, 39], [37, 39], [37, 40],
                [39, 41], [37, 41], [41, 42], [38, 42], [40, 43], [43, 44], [39, 44],
                [35, 44], [38, 45], [44, 45], [26, 45]
            ], 10)

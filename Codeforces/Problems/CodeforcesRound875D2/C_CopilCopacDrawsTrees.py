import bisect
from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import os.path
import sys
input = sys.stdin.readline


MOD = 10**9+7
test = False


def i_int() -> int: return int(input())
def i_str() -> str: return input()[:-1]
def i_array_int() -> List[int]: return list(map(int, input().split()))
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


# class UnionFind_by_rank:
#     root: List[int]
#     rank: List[int]
#     components: int  # Number of distinct components in the graph.

#     def __init__(self, size: int):
#         self.root = [i for i in range(size)]
#         self.rank = [1] * size
#         self.components = size

#     def find(self, x: int):
#         while x != self.root[x]:
#             x = self.root[x]
#         return x

#     def union(self, x: int, y: int):
#         root_x: int = self.find(x)
#         root_y: int = self.find(y)
#         if root_x != root_y:
#             if self.rank[root_x] > self.rank[root_y]:
#                 self.root[root_y] = root_x
#             elif self.rank[root_x] < self.rank[root_y]:
#                 self.root[root_x] = root_y
#             else:
#                 self.root[root_y] = root_x
#                 self.rank[root_x] += 1
#             self.components -= 1

#     def connected(self, x: int, y: int) -> bool:
#         return self.find(x) == self.find(y)

def get_cost(path: List[int], m: Dict[Tuple[int, int], int]):
    lastpos = -1
    path_cost = 1
    for i in range(len(path)-1):
        a, b = path[i], path[i+1]
        if a > b:
            a, b = b, a
        p = m[(a, b)]
        if p < lastpos:
            path_cost += 1
        lastpos = p
    return path_cost


def solve():
    for _ in range(i_int()):
        n = i_int()
        g = i_matrix_int(n-1)
        if n == 2:
            print(1)
            continue

        m = defaultdict(set)
        for pre, cur in g:
            m[pre].add(cur)
            m[cur].add(pre)
        mi = {(min(v[0], v[1]), max(v[0], v[1])): i for i, v in enumerate(g)}

        q = []
        q.append((0, 1, -1, 1))
        resp = 1
        while q:
            pre, cur, last_pos, path_cost = q.pop()
            if pre != 0:
                a, b = pre, cur
                if a > b:
                    a, b = b, a
                p = mi[(a, b)]
                if p < last_pos:
                    path_cost += 1
                last_pos = p
                resp = max(resp, path_cost)

            for nxt in m[cur]:
                q.append((cur, nxt, last_pos, path_cost))
                m[nxt].discard(cur)

        print(resp)


def solve_3():
    """Memory usage too high"""
    for _ in range(i_int()):
        n = i_int()
        g = i_matrix_int(n-1)
        if n == 2:
            print(1)
            continue

        m = defaultdict(set)
        for a, b in g:
            m[a].add(b)
            m[b].add(a)
        mi = {(min(v[0], v[1]), max(v[0], v[1])): i for i, v in enumerate(g)}

        # def rec_cost(cur: int, p: List[int]):
        #     #too many recursions
        #     resp = 1
        #     if len(m[cur]) == 0:
        #         resp = get_cost(p+[cur], mi)
        #     else:
        #         for nxt in m[cur]:
        #             m[nxt].discard(cur)
        #             p.append(cur)
        #             resp = max(resp, rec_cost(nxt, p))
        #             p.pop()
        #     return resp

        # resp = rec_cost(1, [])

        q = []
        q.append((1, []))
        resp = 1
        while q:
            cur, p = q.pop()
            if len(m[cur]) == 0:
                resp = max(resp, get_cost(p+[cur], mi))
            else:
                for nxt in m[cur]:
                    q.append((nxt, p+[cur]))
                    m[nxt].discard(cur)

        print(resp)


def solve_2():
    """Memory usage too high"""
    for _ in range(i_int()):
        n = i_int()
        g = i_matrix_int(n-1)
        if n == 2:
            print(1)
            continue

        m = defaultdict(set)
        for a, b in g:
            m[a].add(b)
            m[b].add(a)

        paths: Dict[int, List[int]] = dict()

        q = []
        q.append((1, []))
        seen = set()
        seen.add(1)
        while q:
            cur, p = q.pop()
            if len(m[cur]) == 1 and cur != 1:
                paths[cur] = p.copy() + [cur]
            else:
                for nxt in m[cur]:
                    if nxt not in seen:
                        q.append((nxt, p+[cur]))
                        seen.add(nxt)

        m = {(min(v[0], v[1]), max(v[0], v[1])): i for i, v in enumerate(g)}

        resp = 1
        for path in paths.values():
            lastpos = -1
            path_cost = 1
            for i in range(len(path)-1):
                a, b = path[i], path[i+1]
                if a > b:
                    a, b = b, a
                p = m[(a, b)]
                if p < lastpos:
                    path_cost += 1
                lastpos = p
            resp = max(resp, path_cost)

        print(resp)


def solve_1():
    """too slow"""
    for _ in range(i_int()):
        n = i_int()
        g = i_matrix_int(n-1)
        if n == 2:
            print(1)
            continue

        resp = 0
        un = set()
        un.add(0)

        while len(un) != n:
            tmp = list()

            for a, b in g:
                if a-1 in un or b-1 in un:
                    un.add(a-1)
                    un.add(b-1)
                else:
                    tmp.append((a, b))
            g = tmp
            resp += 1

        print(resp)


testData = """4
6
4 5
1 3
1 2
3 4
1 6
7
5 6
2 4
2 7
1 3
1 2
4 5
7
6 7
5 6
4 5
3 4
2 3
1 2
2
1 2
1 3
""".split("\n")
# testData = list()
testDataPos = 0

if len(testData) > 1 and os.path.exists('localTestCheckFile.txt'):
    test = True

    def test_data_input():
        global testDataPos
        r = testData[testDataPos]
        testDataPos += 1
        return r
    input = test_data_input


if __name__ == "__main__":
    solve()

from collections import defaultdict
from functools import cache
import heapq
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = dict()
        for i, skills in enumerate(people):
            sk = 0
            for s in skills:
                sk += 2 ** req_skills.index(s)
            m[sk] = i

        q = Deque()
        q.append((0, list()))
        seen = set()
        target = 2 ** len(req_skills) - 1
        seen.add(0)

        while q:
            cur, way = q.popleft()
            if cur == target:
                return [m[w] for w in way]
            for nxt in m.keys():
                if nxt | cur not in seen:
                    q.append((nxt | cur, way + [nxt]))
                    seen.add(nxt | cur)
                    
    def smallestSufficientTeam_2(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = dict()
        for i, skills in enumerate(people):
            sk = 0
            for s in skills:
                sk += 2 ** req_skills.index(s)
            m[sk] = i

        q = Deque()
        q.append((0, list(), set(m.keys()) - {0}))
        seen = set()
        target = 2 ** len(req_skills) - 1
        seen.add(0)

        while q:
            cur, way, s = q.popleft()
            if cur == target:
                return [m[w] for w in way]
            for nxt in s:
                if nxt | cur not in seen:
                    q.append((nxt | cur, way + [nxt], s - {nxt}))
                    seen.add(nxt | cur)

    def smallestSufficientTeam_1(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = dict()
        for i, skills in enumerate(people):
            sk = 0
            for s in skills:
                sk += 2 ** req_skills.index(s)
            m[sk] = i

        q = Deque()
        q.append((0, list()))
        seen = set()
        target = 2 ** len(req_skills) - 1
        while q:
            cur, way = q.popleft()
            if cur == target:
                return [m[w] for w in way]
            if cur in seen:
                continue
            seen.add(cur)
            for nxt in m.keys():
                if nxt | cur not in seen:
                    q.append((nxt | cur, way + [nxt]))


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.smallestSufficientTeam(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0,
            ["java", "nodejs", "reactjs"],
            [["java"],
             ["nodejs"],
             ["nodejs", "reactjs"]],
            [0, 2])
    do_test(1,
            ["algorithms", "math", "java", "reactjs", "csharp", "aws"],
            [["algorithms", "math", "java"],
             ["algorithms", "math", "reactjs"],
             ["java", "csharp", "aws"],
             ["reactjs", "csharp"],
             ["csharp", "math"],
             ["aws", "java"]],
            [1, 2])

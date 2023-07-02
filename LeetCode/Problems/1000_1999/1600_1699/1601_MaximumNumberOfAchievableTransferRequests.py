from collections import defaultdict
from copy import deepcopy
from functools import cache
import itertools
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    """Runtime 74 ms"""

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m: Dict[int, List[int]] = defaultdict(list)
        resp = 0

        for f, t in requests:
            if f == t:
                # The changes of type "from == to" are not considered and immediately added to the result.
                resp += 1
                continue
            m[f].append(t)

        def rings(start: int, m: Dict[int, List[int]]) -> List[List[Tuple[int, int]]]:
            """The function returns all rings that contain the point "start"."""
            q = Deque()
            q.append((start, []))
            resp = []
            while q:
                t, w = q.popleft()
                if len(w) > 0 and t == w[0][0]:
                    # ring found
                    resp += [w]
                    continue
                if t in [f for f, _ in w]:
                    # loop found
                    continue
                if t in m:
                    for nxt in set(m[t]):  # check only unique neighbors -> use "set"
                        q.appendleft((nxt, w+[(t, nxt)]))
            return resp

        def solve(m: Dict[int, List[int]]) -> int:
            """The functiopn gives the best result for the remaining requests"""
            if len(m) == 0:
                return 0
            resp = 0

            for i in range(n):
                if resp > 0:
                    # We are interested only in the first building, which has a ring of requests.
                    # All the remaining rings are processed when the function is called recursively.
                    break
                for ring in rings(i, m):
                    tmp = deepcopy(m)
                    for f, t in ring:
                        tmp[f].remove(t)
                        if len(tmp[f]) == 0:
                            tmp.pop(f)
                    resp = max(len(ring) + solve(tmp), resp)

            return resp

        resp += solve(m)
        return resp

    def maximumRequests_w(self, n: int, requests: List[List[int]]) -> int:
        """Wrong!"""
        m: Dict[int, List[int]] = dict()
        resp = 0

        for f, t in requests:
            if f == t:
                resp += 1
                continue
            if f in m:
                m[f].append(t)
            else:
                m[f] = [t]

        while len(m) > 0:
            check_f = list(m.keys())[0]
            check_t = m[check_f][0]

            q = Deque()
            q.append((check_t, [check_f]))
            SEEN = set()
            ok = False
            longest = []
            while q:
                t, w = q.popleft()
                if t == w[0]:
                    ok = True
                    if len(longest) < len(w):
                        longest = w
                    continue
                if t in SEEN:
                    continue
                SEEN.add(t)
                if t in m:
                    for nxt in m[t]:
                        q.appendleft((nxt, w+[t]))
                        check_f = list(m.keys())[0]
            if not ok:
                m[check_f].pop(0)
                if len(m[check_f]) == 0:
                    m.pop(check_f)
            else:
                ok = True
                resp += len(longest)
                longest += [longest[0]]
                f = longest[0]
                for i in range(1, len(longest)):
                    t = longest[i]
                    m[f].remove(t)
                    if len(m[f]) == 0:
                        m.pop(f)
                    f = t

        return resp


class Solution_i:
    """internat solution:
    https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/solutions/3706092/back-track-c-java-python-beginner-friendly/
    slower than my solution: Runtime 1351 ms
    """

    def __init__(self):
        self.ans = 0

    def helper(self, start, requests, indegree, n, count):
        if start == len(requests):
            for i in range(n):
                if indegree[i] != 0:
                    return
            self.ans = max(self.ans, count)
            return

        # Take
        indegree[requests[start][0]] -= 1
        indegree[requests[start][1]] += 1
        self.helper(start + 1, requests, indegree, n, count + 1)
        indegree[requests[start][0]] += 1
        indegree[requests[start][1]] -= 1

        # Not-take
        self.helper(start + 1, requests, indegree, n, count)

    def maximumRequests(self, n, requests):
        indegree = [0] * n
        self.helper(0, requests, indegree, n, 0)
        return self.ans


class Solution_i2:
    """internet solution:
    https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/solutions/3706208/python-java-c-simple-solution-easy-to-understand/
    Runtime 821 ms
    """

    def maximumRequests(self, n, req):
        for k in range(len(req), 0, -1):
            for c in itertools.combinations(range(len(req)), k):
                degree = [0] * n
                for i in c:
                    degree[req[i][0]] -= 1
                    degree[req[i][1]] += 1
                if not any(degree):
                    return k
        return 0


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.maximumRequests(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, 5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]], 5)
    do_test(1, 3, [[0, 0], [1, 2], [2, 1]], 3)
    do_test(2, 4, [[0, 3], [3, 1], [1, 2], [2, 0]], 4)
    do_test(3, 3, [[1, 2], [2, 2], [0, 0], [1, 1], [0, 2], [0, 0], [2, 1], [0, 1], [1, 0], [2, 2], [0, 1], [2, 0], [2, 2]], 12)
    do_test(4, 4, [[0, 0], [1, 3], [1, 3], [2, 3], [1, 0], [2, 2], [1, 2], [2, 1],
            [1, 3], [0, 2], [3, 0], [3, 1], [2, 2], [3, 0], [0, 3], [3, 1]], 14)
    do_test(5, 3, [[1, 2], [0, 0], [0, 2], [0, 1], [0, 0], [0, 2], [1, 0], [0, 1], [2, 0]], 7)

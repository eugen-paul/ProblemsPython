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
def i_array_str() -> List[str]: return i_str().split()
def i_set_int() -> Set[int]: return set(map(int, input().split()))
def i_matrix_int(h: int) -> List[List[int]]: return [list(map(int, input().split())) for _ in range(h)]


def inv(x): return pow(x % MOD, MOD - 2, MOD)


def solve():
    for _ in range(i_int()):
        n = i_int()
        m: Dict[int, Set[int]] = defaultdict(set)

        for _ in range(n-1):
            f, t = i_array_int()
            m[f].add(t)
            m[t].add(f)

        q = Deque()
        q.append((1, -1))  # 1 is alway a root
        leafs = set()
        while q:
            cur, root = q.pop()
            is_leaf = True
            for nxt in m[cur]:
                if nxt != root:
                    is_leaf = False
                    q.append((nxt, cur))
            if is_leaf:
                leafs.add(cur)

        dp = [0] * (n+1)
        for l in leafs:
            dp[l] = 1

        while leafs:
            nxt_leaf = set()
            for l in leafs:
                for root in m[l]:
                    dp[root] += dp[l]
                    m[root].discard(l)
                    if len(m[root]) == 1 and root != 1:
                        nxt_leaf.add(root)
            leafs = nxt_leaf

        q = i_int()
        for _ in range(q):
            x, y = i_array_int()
            a = dp[x]
            b = dp[y]
            print(a*b)


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = stack.append(f(*args, **kwargs))
            while True:
                try:
                    to = stack.append(stack[-1].send(to))
                except StopIteration as e:
                    stack.pop()
                    to = e.value
                    if not stack:
                        break
            return to

    return wrappedfunc


def solve():
    for _ in range(i_int()):
        n = i_int()
        m: Dict[int, Set[int]] = defaultdict(set)

        for _ in range(n-1):
            f, t = i_array_int()
            m[f].add(t)
            m[t].add(f)

        q = Deque()
        q.append(1)
        while q:
            pos = q.pop()
            for nxt in m[pos]:
                m[nxt].discard(pos)
                q.append(nxt)

        dp = [-1] * (n+1)

        @bootstrap
        def dfs(pos) -> int:
            if dp[pos] != -1:
                return dp[pos]
            resp = 0
            if len(m[pos]) == 0:
                resp = 1
            else:
                for nxt in m[pos]:
                    resp += (yield dfs(nxt))
            dp[pos] = resp
            return resp

        q = i_int()
        for _ in range(q):
            x, y = i_array_int()
            a = dfs(x)
            b = dfs(y)
            print(a*b)


testData = """2
5
1 2
3 4
5 3
3 2
4
3 4
5 1
4 4
1 3
3
1 2
1 3
3
1 1
2 3
3 1
""".split("\n")
testData = """2
5
5 1
1 2
2 3
4 3
2
5 5
5 1
5
3 2
5 3
2 1
4 2
3
4 3
2 1
4 2
""".split("\n")
# testData = """1
# 2
# 1 2
# 1
# 1 1
# """.split("\n")
# testData = list()
testDataPos = 0

if len(testData) > 1 and os.path.exists('localTestCheckFile.txt'):
    test = True

    def test_data_input():
        global testDataPos
        r = testData[testDataPos]
        testDataPos += 1
        return r + "\n"
    input = test_data_input


if __name__ == "__main__":
    solve()

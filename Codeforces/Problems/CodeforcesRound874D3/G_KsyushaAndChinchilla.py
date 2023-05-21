from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter
import sys
input = sys.stdin.readline


def i_array_int() -> List[int]:
    return list(map(int, input().split()))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split())) for _ in range(h)]


MOD = 10**9+7


def inv(x):
    return pow(x % MOD, MOD - 2, MOD)


for _ in range(int(input())):
    n = int(input())
    m = defaultdict(set)
    cnt = [0] * n
    v = dict()
    for i in range(1, n):
        a, b = i_array_int()
        a, b = a-1, b-1
        m[a].add(b)
        m[b].add(a)
        cnt[a] += 1
        cnt[b] += 1
        v[(a, b)] = i
        v[(b, a)] = i

    if min(cnt) == 0:
        print(-1)
        continue

    to_check = {i for i, x in enumerate(cnt) if x == 1}

    resp = list()
    impossible = False
    while to_check and not impossible:
        nxt_round_check = set()
        while to_check and not impossible:
            cur = to_check.pop()
            if len(m[cur]) != 1:
                impossible = True
                break

            mid = m[cur].pop()  # the node has just one nb
            mid_set = m[mid]

            if len(mid_set) == 1:  # segment with only two nodes (cur + nb) => imposible
                impossible = True
                break
            elif len(mid_set) == 2:
                mid_set.remove(cur)
                end = mid_set.pop()
                end_set = m[end]
                if len(end_set) == 1:
                    to_check.discard(end)
                    nxt_round_check.discard(end)
                for end_nb in end_set:
                    if end_nb == mid:
                        continue
                    resp.append(v[(end, end_nb)])
                    m[end_nb].discard(end)
                    cnt[end_nb] -= 1
                    if cnt[end_nb] == 1:
                        nxt_round_check.add(end_nb)
                    elif cnt[end_nb] == 0:
                        impossible = True
                        break
            else:
                end = -1
                for mid_nb in mid_set:
                    if mid_nb == cur:
                        continue
                    if cnt[mid_nb] == 1:
                        end = mid_nb
                        break
                if end >= 0:
                    for mid_nb in mid_set:
                        if mid_nb == cur or mid_nb == end:
                            continue
                        resp.append(v[mid, mid_nb])
                        cnt[mid_nb] -= 1
                        m[mid_nb].discard(mid)
                        if cnt[mid_nb] == 1:
                            nxt_round_check.add(mid_nb)
                        elif cnt[mid_nb] == 0:
                            impossible = True
                            break
                    to_check.discard(end)
                    nxt_round_check.discard(end)
                else:
                    nxt_round_check.add(cur)
                    m[cur].add(mid)
        to_check = nxt_round_check

    if impossible:
        print(-1)
    else:
        print(len(resp))
        print(" ".join([str(x) for x in resp]))

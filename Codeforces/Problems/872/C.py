from collections import defaultdict
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter


def i_array_int() -> List[int]:
    return list(map(int, input().split(" ")))


def i_matrix_int(h: int) -> List[List[int]]:
    return [list(map(int, input().split(" "))) for _ in range(h)]


"""
From Editorial:
First we can notice that, if someone with a specific favourite seat(i.e. not -1 nor -2) has got his seat taken by a -1 guy or a -2 guy, 
it's better to let the first man go first, and the -1 or -2 one go after him.

Now, we know it's better to make those with a favourite seat go in first. After they have seated, 
now we consider filling the space between them with -1 and -2. It's easy to notice that we can find two non-overlapping prefix 
and suffix, and fill the blank seats in the prefix with -1, and the blanks in the suffix with -2. 
We now only need to find the answer greedily for each division point between the prefix and the suffix.
"""

# for _ in range(int(input())):
#     n, m = i_array_int()
#     a = i_array_int()
#     cntL = 0
#     cntR = 0
#     b = [0] * m
#     for c in a:
#         if c == -1:
#             cntL += 1
#         elif c == -2:
#             cntR += 1
#         else:
#             b[c-1] += 1

#     nowL, nowR, vis = 0, 0, 0
#     for i in range(m):
#         if b[i] > 0:
#             vis += 1
#         else:
#             nowR += 1

#     resp = max(cntL, cntR) + vis
#     for i in range(m):
#         if b[i] > 0:
#             resp = max(
#                 resp,
#                 min(cntL, nowL) + min(cntR, nowR) + vis
#             )
#         else:
#             nowL += 1
#             nowR -= 1
#     resp = min(resp, m)

#     print(resp)

# # internet solution
# t = False
# if t:
# for _ in range(int(input())):
#     n, m = i_array_int()
#     a = i_array_int()
#     c1 = a.count(-1)
#     c2 = a.count(-2)

#     s = list({x for x in a if x > 0})
#     s.sort()
#     nn = len(s)

#     resp = max(
#         min(m, nn+c1),
#         min(m, nn+c2)
#     )
#     for i in range(nn):
#         resp = max(
#             resp,
#             1 + min(s[i] - 1, i + c1) + min(m - s[i], nn - i - 1 + c2)
#         )
#     print(resp)


# internet solution
# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     l = r = 0
#     xx = []
#     for x in map(int, input().split()):
#         if x == -1:
#             l += 1
#         elif x == -2:
#             r += 1
#         else:
#             xx.append(x)
#     xx = sorted(set(xx))
#     ans = max(l+len(xx), r+len(xx))
#     ans = min(ans, m)
#     for i, x in enumerate(xx):
#         candl = i + l
#         candl = min(candl, x-1)
#         candr = len(xx)-i-1 + r
#         candr = min(candr, m-x)
#         cand = candl + candr + 1
#         ans = max(ans, cand)
#         ans = min(ans, m)
#     print(ans)

for _ in range(int(input())):
    n, m = i_array_int()
    a = i_array_int()
    lefts = a.count(-1)
    rights = a.count(-2)
    middles = sorted(set(filter(lambda x: x > 0, a)))
    ans = 0
    for i in range(len(middles)):  # try to start at every possible middle
        x = middles[i]
        left_elems = min(
            x - 1,     # There is a x-1 places left
            lefts + i  # if all "lefts" are allocated optimally, then a maximum of lefts+i places are occupied on the left side.
        )
        right_elems = min(
            m - x,     # There is a m - x places right
            rights + ((len(middles) - 1) - i)
        )

        ans = max(ans, left_elems + right_elems + 1)  # fill left and right

    # if we start at left or right, we cannot fill the other guy anymore
    ans = max(ans, min(m, lefts + len(middles)))  # start at left
    ans = max(ans, min(m, rights + len(middles)))  # start at right

    print(ans)

from collections import defaultdict
from functools import cache
import itertools
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:

    def largestVariance(self, s: str) -> int:
        s = [ord(c)-ord("a") for c in s]
        c = set(s)

        def solve(a: int, b: int) -> int:
            l, cnt_a, cnt_b, resp = 0, 0, 0, 0

            for c in s:
                if c != a and c != b:
                    continue
                cnt_a += 1 if c == a else 0
                cnt_b += 1 if c == b else 0
                while (cnt_b > 0 and cnt_a > 0 and cnt_b > cnt_a) or (cnt_b >= 2 and s[l] == b) or (s[l] != a and s[l] != b):
                    cnt_a -= 1 if s[l] == a else 0
                    cnt_b -= 1 if s[l] == b else 0
                    l += 1
                if cnt_a > 0 and cnt_b > 0:
                    resp = max(resp, cnt_a-cnt_b)
            return resp

        resp = 0
        for a in c:
            for b in c:
                if a == b:
                    continue
                resp = max(resp, solve(a, b))
        return resp

    def largestVariance_i(self, s: str) -> int:
        """internat solution:
        https://leetcode.com/problems/substring-with-largest-variance/solutions/2786797/python3-explanation/
        """
        # This is similar to the Kadane's algorithm, see problem 53 before attempting this one
        # Here we take every permutation of 2 characters in a string and then apply Kadane algo to it Say string is 'abcdab'
        # From the perspective of characters a, b the string is +1, -1, +0, +0, +1, -1
        # and we want to maximize this sum note that we also want to make sure both a and b are in there, otherwise the numbers will be incorrect.
        # Also, our operation of finding the sum is not commutative, so we need permutations and not combinations.
        cntr = Counter(s)
        res = 0
        for a, b in itertools.permutations(cntr, 2):
            a_cnt, b_cnt = cntr[a], cntr[b]
            var = 0
            seen_a = seen_b = False

            for c in s:
                # this won't impact the variance -- so ignore
                if c not in (a, b):
                    continue
                if var < 0:
                    # we have more b's than a's
                    # if no more a's left, var would ultimately be -ve -- so break
                    if not a_cnt:
                        break
                    # just add the remaining a's to var
                    if not b_cnt:
                        res = max(res, var + a_cnt)
                        break
                    # we have a's and b's remaining, so restart
                    seen_a = seen_b = False
                    var = 0
                if c == a:
                    var += 1
                    a_cnt -= 1
                    seen_a = True
                if c == b:
                    var -= 1
                    b_cnt -= 1
                    seen_b = True
                if seen_a and seen_b:
                    res = max(res, var)
        return res


def do_test(i: int, s, r):
    c = Solution()
    resp = c.largestVariance(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "aababbb", 3)
    do_test(1, "abcde", 0)
    do_test(2, "bbbaaaa", 3)
    do_test(3, "aaabbbb", 3)
    do_test(4, "aaabcbdbebf", 3)
    do_test(5, "aaaaa", 0)
    do_test(6, "bbabaaa", 3)
    do_test(7, "ykudzhiixwttnvtesiwnbcjmsydidttiyabbwzlfbmmycwjgzwhbtvtxyvkkjgfehaypiygpstkhakfasiloaveqzcywsiujvixcdnxpvvtobxgroznswwwipypwmdhldsoswrzyqthaqlbwragjrqwjxgmftjxqugoonxadazeoxalmccfeyqtmoxwbnphxih", 12)
    do_test(8, "baabaa", 3)

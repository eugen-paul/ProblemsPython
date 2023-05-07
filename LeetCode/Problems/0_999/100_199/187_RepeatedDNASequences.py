from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        seen = set()
        resp = set()

        for i in range(len(s)-9):
            dna = s[i:i+10]
            if dna in seen:
                resp.add(dna)
            seen.add(dna)

        return list(resp)

    def findRepeatedDnaSequences_1(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        count = Counter()
        dna: str = s[:10]
        count[dna] += 1

        for i in range(10, len(s)):
            dna = dna[1:] + s[i]
            count[dna] += 1

        resp = [k for k, v in count.items() if v > 1]
        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.findRepeatedDnaSequences(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"])
    do_test(1, "AAAAAAAAAAAAA", ["AAAAAAAAAA"])
    do_test(2, "AAAAAAAAAAA", ["AAAAAAAAAA"])

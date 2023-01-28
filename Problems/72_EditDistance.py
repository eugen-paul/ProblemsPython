import heapq
from typing import Deque, Dict, List, Set, Tuple


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def get_subs(a: str, b: str) -> Tuple[str, str]:
            sub_w1 = a
            sub_w2 = b
            for _ in range(min(len(sub_w1), len(sub_w2))):
                if sub_w1[0] != sub_w2[0]:
                    break
                sub_w1 = sub_w1[1:]
                sub_w2 = sub_w2[1:]
            return (sub_w1, sub_w2)

        word1, word2 = get_subs(word1, word2)

        # current cost, word1, word2
        to_check: List[Tuple[int, str, str]] = list()
        heapq.heappush(to_check, (0, word1, word2))

        best = max(len(word1), len(word2))

        old: Set[Tuple[str, str]] = set()

        while to_check:
            cost, w1, w2 = heapq.heappop(to_check)
            if cost + abs(len(w1) - len(w2)) >= best:
                continue

            if len(w1) == 0 or len(w2) == 0:
                best = min(best, cost + max(len(w1), len(w2)))
                continue

            if (w1, w2) in old:
                continue
            old.add((w1, w2))

            # do update
            sub_w1, sub_w2 = get_subs(w1[1:], w2[1:])
            heapq.heappush(to_check, (cost+1, sub_w1, sub_w2))

            # do delete
            sub_w1, sub_w2 = get_subs(w1[1:], w2)
            heapq.heappush(to_check, (cost+1, sub_w1, sub_w2))

            # do insert
            sub_w1, sub_w2 = get_subs(w1, w2[1:])
            heapq.heappush(to_check, (cost+1, sub_w1, sub_w2))

        return best

    def minDistance_2(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        if len(word1) < len(word2):
            word1, word2 = word2, word1

        if word1 == word2:
            return 0

        def get_subs(a: str, b: str) -> Tuple[str, str]:
            sub_w1 = a
            sub_w2 = b
            for _ in range(min(len(sub_w1), len(sub_w2))):
                if sub_w1[0] != sub_w2[0]:
                    break
                sub_w1 = sub_w1[1:]
                sub_w2 = sub_w2[1:]
            return (sub_w1, sub_w2)

        word1, word2 = get_subs(word1, word2)

        # current cost, word1, word2
        to_check: List[Tuple[int, str, str]] = list()
        heapq.heappush(to_check, (0, word1, word2))

        best = max(len(word1), len(word2))

        old: Set[Tuple[str, str]] = set()

        while to_check:
            cost, w1, w2 = heapq.heappop(to_check)
            rest_min_cost = abs(len(w1) - len(w2))
            if cost + rest_min_cost >= best:
                continue

            if len(w1) == 0 and len(w2) == 0:
                best = min(best, cost)
                continue

            if len(w1) == 0 or len(w2) == 0:
                best = min(best, cost + max(len(w1), len(w2)))
                continue

            if (w1, w2) in old:
                continue

            old.add((w1, w2))

            # do update
            sub_w1 = w1[1:]
            sub_w2 = w2[1:]
            sub_w1, sub_w2 = get_subs(sub_w1, sub_w2)
            heapq.heappush(to_check, (cost+1, sub_w1, sub_w2))

            # do delete
            sub_w1 = w1[1:]
            sub_w2 = w2
            sub_w1, sub_w2 = get_subs(sub_w1, sub_w2)
            heapq.heappush(to_check, (cost+1, sub_w1, sub_w2))

            # do insert
            sub_w1 = w1
            sub_w2 = w2[1:]
            sub_w1, sub_w2 = get_subs(sub_w1, sub_w2)
            heapq.heappush(to_check, (cost+1, sub_w1, sub_w2))

        return best


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.minDistance(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "horse", "ros", 3)
    do_test(1, "intention", "execution", 5)
    do_test(2, "abcdefg", "abcdefg", 0)
    do_test(3, "abcdefg", "kabcdefg", 1)
    do_test(4, "abcdefg", "kabcdef", 2)
    do_test(5, "abcdefg", "klmnopq", 7)
    do_test(6, "aaaaaaa", "aaabaaa", 1)
    do_test(7, "abcdefg", "kabczdefg", 2)
    do_test(8, "aaaabbb", "aaaacbbe", 2)

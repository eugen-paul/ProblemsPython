from typing import Counter, Dict, List, Set, Tuple


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        count_first = Counter()
        ends: Dict[str, Set[str]] = dict()
        starts = Counter()

        for w in ideas:
            count_first[w[0]] += 1
            end = w[1:]
            if end in ends:
                for x in ends[end]:
                    starts[(w[0], x)] += 1
                    starts[(x, w[0])] += 1
                ends[end].add(w[0])
            else:
                ends[end] = {w[0]}

        resp = 0
        for w in ideas:
            st = w[0]
            end = w[1:]
            names_count = len(ideas)
            for c, n in count_first.items():
                if c in ends[end]:
                    names_count -= n
                elif (c, st) in starts:
                    names_count -= starts[(c, st)]

            resp += names_count

        return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.distinctNames(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["coffee", "donuts", "time", "toffee"], 6)
    do_test(1, ["lack", "back"], 0)
    do_test(2, ["coffee", "donuts", "zotuts", "time", "toffee"], 14)
    do_test(3, ["coffee", "donuts", "conuts", "time", "toffee"], 6)

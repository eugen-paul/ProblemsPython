from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {c: i for i, c in enumerate(order)}
        repl = [[m[c] for c in w] for w in words]
        return repl == sorted(repl)
    
    def isAlienSorted_internet(self, words: List[str], order: str) -> bool:
        m = {c: i for i, c in enumerate(order)}
        repl = [[m[c] for c in w] for w in words]
        return all ( x <= y for (x,y) in zip(repl, repl[1:]))

    def isAlienSorted_1(self, words: List[str], order: str) -> bool:
        repl = []
        for w in words:
            sub_w = [order.index(x) for x in w]
            repl.append(sub_w)
        return repl == sorted(repl)


def do_test(i: int, s, n, r):
    c = Solution()
    resp = c.isAlienSorted(s, n)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True)
    do_test(1, ["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False)
    do_test(2, ["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False)
    do_test(3, ["abc", "abc"], "abcdefghijklmnopqrstuvwxyz", True)

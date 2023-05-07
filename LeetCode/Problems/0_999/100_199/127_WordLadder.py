from collections import defaultdict
from typing import Deque, List, Dict, Set, Tuple, Counter


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m: Dict[str, List[str]] = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                m[word[:i] + "X" + word[i+1:]].append(word)

        paths: Dict[str, int] = dict()
        paths[beginWord] = 1
        to_check = Deque()
        to_check.append((beginWord, 1))

        while to_check:
            word, cost = to_check.popleft()

            next_words = set()
            for i in range(len(word)):
                next_words.update(m[word[:i] + "X" + word[i+1:]])

            for w in next_words:
                if paths.get(w, 10000) > cost:
                    paths[w] = cost + 1
                    to_check.append((w, cost+1))

        return paths.get(endWord, 0)


def do_test(i: int, s, n, l, r):
    c = Solution()
    resp = c.ladderLength(s, n, l)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5)
    do_test(1, "hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0)
    do_test(2, "hit", "hit", ["hot", "dot", "dog", "lot", "log"], 1)

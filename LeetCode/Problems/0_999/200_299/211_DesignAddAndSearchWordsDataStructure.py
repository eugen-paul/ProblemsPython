from collections import defaultdict
from typing import List


class MyTree:

    childs: List['MyTree']

    def __init__(self):
        self.childs = [None] * 27
        self.childs[-1] = False

    def contains(self, word: str, dots: int = 0) -> bool:
        if len(word) == 0:
            return self.childs[-1]

        if word[0] != '.':
            if self.childs[ord(word[0]) - ord('a')]:
                return self.childs[ord(word[0]) - ord('a')].contains(word[1:], dots)
        else:
            if dots == 3:
                return False
            for i in range(26):
                if self.childs[i] and self.childs[i].contains(word[1:], dots+1):
                    return True

        return False

    def add(self, word: str) -> None:
        if len(word) == 0:
            self.childs[-1] = True
            return

        if not self.childs[ord(word[0]) - ord('a')]:
            self.childs[ord(word[0]) - ord('a')] = MyTree()

        self.childs[ord(word[0]) - ord('a')].add(word[1:])


class WordDictionary:

    tree: MyTree

    def __init__(self):
        self.tree = MyTree()

    def addWord(self, word: str) -> None:
        self.tree.add(word)

    def search(self, word: str) -> bool:
        return self.tree.contains(word, 0)


def do_test(i: int, s, r, n):
    c: WordDictionary
    res = True
    for nr, command in enumerate(s):
        if command == "WordDictionary":
            c = WordDictionary()
        elif command == "addWord":
            c.addWord(r[nr][0])
        elif command == "search":
            if c.search(r[nr][0]) != n[nr]:
                print("error search")
                res = False
        else:
            print("")
    if res:
        print("OK", i)
    else:
        print("ERROR", i)

class WordDictionary:
    """Alternative internet solution"""
    def __init__(self):
        self.words = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.words[len(word)].append(word)

    def search(self, word: str) -> bool:
        n = len(word)
        if '.' in word:
            for w in self.words[n]:
                if all(word[i] in (w[i], '.') for i in range(n)):
                    return True
            return False
        return word in self.words[n]

if __name__ == "__main__":
    do_test(0,
            ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
            [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            [None, None, None, None, False, True, True, True]
            )
    do_test(1,
            ["WordDictionary", "addWord", "search", "search"],
            [[], ["a"], ["a"], ["."]],
            [None, None, True, True]
            )
    do_test(2,
            ["WordDictionary", "addWord", "search", "search", "search", "search"],
            [[], ["aaaa"], ["aaaa"], [".aaa"], [".a.."], ["...."]],
            [None, None, True, True, True, False]
            )


from collections import defaultdict
from functools import cache
from math import inf
from typing import Deque, List, Dict, Set, Tuple, Counter

# import sys
# sys.setrecursionlimit(10000)


class MyTree:

    childs: List

    def __init__(self):
        self.childs = [None] * 27
        self.childs[-1] = False

    def contains(self, word: str) -> bool:
        if len(word) == 0:
            return self.childs[-1]
        if self.childs[ord(word[0]) - ord('a')]:
            return self.childs[ord(word[0]) - ord('a')].contains(word[1:])
        return False

    def startWith(self, word: str) -> bool:
        if len(word) == 0:
            return True
        if self.childs[ord(word[0]) - ord('a')]:
            return self.childs[ord(word[0]) - ord('a')].startWith(word[1:])
        return False

    def add(self, word: str) -> None:
        if len(word) == 0:
            self.childs[-1] = True
            return

        if not self.childs[ord(word[0]) - ord('a')]:
            self.childs[ord(word[0]) - ord('a')] = MyTree()

        self.childs[ord(word[0]) - ord('a')].add(word[1:])


class Trie:
    tree: MyTree

    def __init__(self):
        self.tree = MyTree()

    def insert(self, word: str) -> None:
        self.tree.add(word)

    def search(self, word: str) -> bool:
        return self.tree.contains(word)

    def startsWith(self, prefix: str) -> bool:
        return self.tree.startWith(prefix)


class Trie_1:
    full: Set[str]
    sub: Set[str]

    def __init__(self):
        self.full = set()
        self.sub = set()

    def insert(self, word: str) -> None:
        self.full.add(word)
        for i in range(len(word)-1):
            self.sub.add(word[:i+1])

    def search(self, word: str) -> bool:
        return word in self.full

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.sub or prefix in self.full


def do_test(i: int, s, r, n):
    c: Trie
    res = True
    for nr, command in enumerate(s):
        if command == "Trie":
            c = Trie()
        elif command == "insert":
            c.insert(r[nr][0])
        elif command == "search":
            if c.search(r[nr][0]) != n[nr]:
                print("error search")
                res = False
        elif command == "startsWith":
            if c.startsWith(r[nr][0]) != n[nr]:
                print("error startsWith")
                res = False
        else:
            print("")
    if res:
        print("OK", i)
    else:
        print("ERROR", i)


if __name__ == "__main__":
    do_test(0,
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True]
            )
    do_test(1,
            ["Trie", "insert", "search", "startsWith"],
            [[], ["a"], ["a"], ["a"]],
            [None, None, True, True]
            )
